
import React, { useState } from 'react';
import './Style.css'
import WebcamComponent from './WebcamComponent'
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import { styled } from '@mui/material/styles';
import VideoUpload from './VideoUpload'

import Box from '@mui/material/Box';
import Grid from '@mui/material/Unstable_Grid2';
import Paper from '@mui/material/Paper';
import Training from './Training';



export default function Practice() {  
    const [currentComponent, setCurrentComponent] = useState('upload');
    const handleButtonClick = (component) => {
        setCurrentComponent(component);
      };

    return (
    <div style={{margin: 0}}>
        <h2>Practice</h2>

        {currentComponent === 'upload' && <VideoUpload />}
        {currentComponent === 'dropzone' && <WebcamComponent />}    

        <Box height={150} justifyContent="center" width={600} my={4} display="flex"alignItems="center" gap={4}>
        <Grid container spacing={2}>
            <Grid xs={5} md={6}>
                <Button size="large" variant="contained" onClick={() => handleButtonClick('upload')}>Upload Video</Button>
            </Grid>
            <Grid xs={5} md={6}>
                <Button size="large" variant="contained" onClick={() => handleButtonClick('live')}>Live Video</Button>
            </Grid>
            <Grid xs={5} md={6}>
                <Button size="large" variant="contained" href='/results'>View Results</Button>
            </Grid>
            <Grid xs={5} md={6}>
                <Button size="large" variant="contained">Feedback</Button>
            </Grid>
            <Grid xs={5} md={12}>
                <Button size="large" variant="contained" href='/training'>Back to Training Page</Button>
            </Grid>
        </Grid>
        </Box>

    </div>

    )
  }

  
