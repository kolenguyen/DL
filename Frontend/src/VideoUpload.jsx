import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Results from './Results';

const VideoUpload = () => {
  const [uploadedFiles, setUploadedFiles] = useState([]);
  const [uploadResults, setUploadResults] = useState(null);

  const onDrop = (acceptedFiles) => {
    setUploadedFiles(acceptedFiles);
  };

  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    accept: ['video/*', 'image/*'], 
  });

   const handleUpload = () => {
    const formData = new FormData();
    uploadedFiles.forEach((file) => {
      formData.append('file', file);
    });

    fetch('http://127.0.0.1:5000/practice/upload', {
      method: 'POST',
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('Upload success:', data);
        console.log('Upload success:', data['message']);
        // uploadResults=data['message'];
        const d = data['message'];
        setUploadResults(d);
        // console.log(uploadResults);
      })
      .catch((error) => {
        console.error('Upload error:', error);
        setUploadResults(null);
      });
  };

  return (
    <div>
      <Paper elevation={3} style={{ padding: 20, textAlign: 'center' }}>
        <div {...getRootProps()} style={{ cursor: 'pointer', padding: '20px', border: '2px dashed #ccc' }}>
          <input {...getInputProps()} />
          <Typography variant="body1" color="textSecondary">
            Drag & Drop or click to upload video or image
          </Typography>
        </div>
        {uploadedFiles.length > 0 && (
          <div>
            <Typography variant="subtitle1" color="textPrimary" style={{ marginTop: '10px' }}>
              Uploaded Files:
            </Typography>
            <ul>
              {uploadedFiles.map((file) => (
                <li key={file.name}>{file.name}</li>
              ))}
            </ul>
          </div>
        )}
         <Button variant="contained" color="primary" onClick={handleUpload}>
          Analize
        </Button>
        <Button variant="contained" color="primary" onClick={() => setUploadedFiles([])}>
          Clear
        </Button>
      </Paper>
      {/* iisue */}
      { <Results data={uploadResults}/>}
      {/* {uploadResults} */}
    </div>
  );
};

export default VideoUpload;
