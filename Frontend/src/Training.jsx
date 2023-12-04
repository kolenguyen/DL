import React, { useState } from 'react';
import ElementList from './ElementList'
import './Style.css'
import VideoComponent from './VideoComponent'
import Grid from '@mui/material/Grid';

export default function Training() {  
    const [selectedVideoUrl, setSelectedVideoUrl] = useState(null);
    
    const handleItemClick = (url) => {
      setSelectedVideoUrl(url);
    };
    
    return (
    <div style={{margin: 0}}>
      <h2>Training</h2>
      <Grid container spacing={26}>
        <Grid item xs={6}>
          <ElementList  onItemClicked={handleItemClick}/>
        </Grid>
        <Grid item xs={6} style={{ textAlign: 'right'}}>
          <VideoComponent videoURL={selectedVideoUrl}/>
        </Grid>
      </Grid>
    </div>
    )
  }
  
