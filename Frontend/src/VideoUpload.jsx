import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

const VideoUpload = () => {
  const [uploadedFiles, setUploadedFiles] = useState([]);

  const onDrop = (acceptedFiles) => {
    setUploadedFiles(acceptedFiles);
  };

  const { getRootProps, getInputProps } = useDropzone({ onDrop, accept: 'video/*' });

  return (
    <div>
      <Paper elevation={3} style={{ padding: 20, textAlign: 'center' }}>
        <div {...getRootProps()} style={{ cursor: 'pointer', padding: '20px', border: '2px dashed #ccc' }}>
          <input {...getInputProps()} />
          <Typography variant="body1" color="textSecondary">
            Drag & Drop or click to upload videos
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
        <Button variant="contained" color="primary" onClick={() => setUploadedFiles([])}>
          Clear
        </Button>
      </Paper>
    </div>
  );
};

export default VideoUpload;
