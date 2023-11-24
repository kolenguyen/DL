
import './Style.css'
import WebcamComponent from './WebcamComponent'
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import { styled } from '@mui/material/styles';

import Box from '@mui/material/Box';
import Grid from '@mui/material/Unstable_Grid2';
import Paper from '@mui/material/Paper';



export default function Practice() {  
    return (
    <div style={{margin: 0}}>
        <h2>Practice</h2>
        <WebcamComponent/>
        <Box height={150} justifyContent="center" width={600} my={4} display="flex"alignItems="center" gap={4}>
        <Grid container spacing={2}>
            <Grid xs={5} md={6}>
                <Button size="large" variant="outlined">Upload Video</Button>
            </Grid>
            <Grid xs={5} md={6}>
                <Button size="large" variant="outlined">Live Video</Button>
            </Grid>
            <Grid xs={5} md={6}>
                <Button size="large" variant="outlined">Results</Button>
            </Grid>
            <Grid xs={5} md={6}>
                <Button size="large" variant="outlined">Feedback</Button>
            </Grid>
            <Grid xs={5} md={12}>
                <Button size="large" variant="outlined">Back to Training Page</Button>
            </Grid>
        </Grid>
        </Box>

    </div>

    )
  }

  
