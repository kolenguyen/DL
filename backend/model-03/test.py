import cv2
import openvino as ov
import os
import numpy as np
import json
import argparse

def process_image(input_image, roi, input_width, input_height):
    """Converts input image according to model requirements"""
    cropped_image = input_image[int(roi[1]):int(roi[3]), int(roi[0]):int(roi[2])]
    resized_image = cv2.resize(cropped_image, (input_width, input_height))
    out_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    # print(f'The shape of an image is is {out_image.shape}')
    return out_image.transpose(2, 0, 1).astype(np.float32)

def prepare_net_input(images, person_roi):
    """Converts input sequence of images into blob of data"""
    data = np.stack([process_image(img, person_roi, 224, 224) for img in images], axis=0)
    data = data.reshape((1,) + data.shape)
    data = np.transpose(data, (0, 2, 1, 3, 4))
    # print(f'The shape of image stack is {data.shape}')
    return data

# find roi or region of interest for 224 x 224 img
def convert_to_central_roi():
    """Extracts from the input ROI the central square part with specified side size"""
    input_height = 224
    input_width = 224
    img_scale = 256
    src_roi = [
        input_width * 0,
        input_height * 0,
        input_width * 1,
        input_height* 1
    ]

    src_roi_height, src_roi_width = src_roi[3] - src_roi[1], src_roi[2] - src_roi[0]
    src_roi_center_x = 0.5 * (src_roi[0] + src_roi[2])
    src_roi_center_y = 0.5 * (src_roi[1] + src_roi[3])

    height_scale = float(input_height) / float(img_scale)
    width_scale = float(input_width) / float(img_scale)
    assert height_scale < 1.0
    assert width_scale < 1.0

    min_roi_size = min(src_roi_height, src_roi_width)
    trg_roi_height = int(height_scale * min_roi_size)
    trg_roi_width = int(width_scale * min_roi_size)

    trg_roi = [int(src_roi_center_x - 0.5 * trg_roi_width),
                int(src_roi_center_y - 0.5 * trg_roi_height),
                int(src_roi_center_x + 0.5 * trg_roi_width),
                int(src_roi_center_y + 0.5 * trg_roi_height)]

    return trg_roi

# Path to the OpenVINO IR (Intermediate Representation) files
model_xml = 'asl-recognition-0004/FP16/asl-recognition-0004.xml'
model_bin = 'asl-recognition-0004/FP16/asl-recognition-0004.bin'

# def main():
    #Get video path from command lane
parser = argparse.ArgumentParser(description="Process an MP4 video")
parser.add_argument("video_path", help="Path to mp4 video file")
video_path = parser.parse_args().video_path
print(video_path)
#Create core object
core = ov.Core()

#Read a model from a drive/ location
model = core.read_model(model=model_xml)

#checking the model input
# input_layer = model.inputs
# for i in input_layer:
#     print(f'{i}')
# <Output: names[input] shape[1,3,16,224,224] type: f32>
# model.reshape([1,3,-1,224,224])

#Break video into frames
output_directory = os.path.join('output_frames',video_path)
os.makedirs(output_directory, exist_ok=True)

# Open video file
cap = cv2.VideoCapture(video_path)

#read and save each frame
frame_number = 0
while True:
    ret, frame = cap.read()

    # Break the loop if we have reached the end of the video
    if not ret:
        break

    # Save the frame as an image file
    frame_path = os.path.join(output_directory, f"frame_{frame_number}.png")
    cv2.imwrite(frame_path, frame)

    frame_number += 1

# Release the video capture object
cap.release()
print(f"{frame_number} frames saved successfully.")

#using frames to fill the tensor input data
images = []
frames= [frame for frame in os.listdir(output_directory) if os.path.isfile(os.path.join(output_directory,frame)) ]
len_frames= len(frames)
person_roi = convert_to_central_roi()
if (len_frames > 0):
    for frame in frames:
        frame_path = os.path.join(output_directory,frame)
        image = cv2.imread(frame_path)
#         #resize to 224x224
#         image = cv2.resize(image, (224,224))
#         # print(f'checking {image.shape}')
        # image_height = image.shape[0]
        # image_width = image.shape[1]
        images.append(image)
else:
    raise ValueError("Frames are 0-length")

process_images= prepare_net_input(images, person_roi)
model.reshape([1,3,len_frames,224, 224])

#Load a model to device
compiled_model= core.compile_model(model=model, device_name = "CPU")

#Create an inference request
infer_request = compiled_model.create_infer_request()

# print(image_height)
# print(image_width)
# print(image_frames)
# model.reshape([1,3, image_frames, 228, 228])
# print("checkpoint ")
# input_tensor = infer_request.get_input_tensor(0)
# input_tensor.data.shape = (1,3,201, 224, 224)
# print(f"input_tensor data type: {input_tensor.data.dtype}")
# assert input_tensor.data.dtype == np.float32

# image_data = np.array(data)
# trimmed_data = image_data
# print(f"trimmed data shape:{trimmed_data.shape}")
# reshaped_array = np.transpose(trimmed_data, (3, 0, 1, 2))
# input_data = reshaped_array.reshape((1,3,image_frames,224,224))
# print(f"input tensor data shape:{input_tensor.shape}")
# np.copyto(input_tensor.data,input_data)

#Start inference
results = infer_request.infer(process_images)
# print(results)
#Process inference result
output_tensor = infer_request.get_output_tensor()
# assert output_tensor.data.dtype == np.int32
# print(f"out_tensor data type: {output_tensor.data.dtype}")
# print(f"out_tensor data type: {output_tensor.data}")
logits = output_tensor.data[0]
predicted = np.argmax(logits)


with open('msasl100.json','r') as file:
    labels = json.load(file)

print(f"predict label is: {labels[predicted]} with {np.max(logits)* 100}%")
# if __name__ == '__main__':
#     main()