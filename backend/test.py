import cv2
# import openvino as ov
import os
import numpy as np
import json

# Path to the OpenVINO IR (Intermediate Representation) files
model_xml = 'asl-recognition-0004/FP16/asl-recognition-0004.xml'
model_bin = 'asl-recognition-0004/FP16/asl-recognition-0004.bin'

#Crate core object
import openvino as ov
core = ov.Core()

#Read a model from a drive/ location
model = core.read_model(model=model_xml)
#Load a model to device
compiled_model= core.compile_model(model=model, device_name = "CPU")
#checking the model input
input_layer = model.input(0)
print(f"input precision: {input_layer.element_type}")
print(f"input shape: {input_layer.shape}")
#Create an inference request
infer_request = compiled_model.create_infer_request()
#Read and process input - testing
red_path = 'test_inputs/red_frames/'
data = []
red_frames= [frame for frame in os.listdir(red_path) if os.path.isfile(os.path.join(red_path,frame)) ]
print(f'If {len(red_frames)} is 201, this is correct')
for frame in red_frames:
    frame_path = os.path.join(red_path,frame)
    image = cv2.imread(frame_path)
    #resize to 224x224
    image = cv2.resize(image, (224,224))
    # print(f'checking {image.shape}')
    data.append(image)

input_tensor = infer_request.get_input_tensor(0)
# input_tensor.data.shape = (1,3,201, 224, 224)
# print(f"input_tensor data type: {input_tensor.data.dtype}")
# assert input_tensor.data.dtype == np.float32

image_data = np.array(data)
trimmed_data = image_data [:16]
# print(f"trimmed data shape:{trimmed_data.shape}")
reshaped_array = np.transpose(trimmed_data, (3, 0, 1, 2))
input_data = reshaped_array.reshape((1,3,16,224,224))
np.copyto(input_tensor.data,input_data)

#Start inference
results = infer_request.infer()
#Process inference result
output_tensor = infer_request.get_output_tensor()
# assert output_tensor.data.dtype == np.int32
print(f"out_tensor data type: {output_tensor.data.dtype}")
print(f"out_tensor data type: {output_tensor.data}")
logits = output_tensor.data[0]
predicted = np.argmax(logits)


with open('msasl100.json','r') as file:
    labels = json.load(file)

print(f"predict label is: {labels[predicted]}")