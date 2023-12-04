
import ElementList from './ElementList'
import './Style.css'
import VideoComponent from './VideoComponent'
import Grid from '@mui/material/Grid';

export default function Training() {  
    const youtubeVideoURL = 'https://www.youtube.com/embed/0FcwzMq4iWg?si=jh_ljIhlbkmiGvcK';

    return (
    <div style={{margin: 0}}>
      <h2>Training</h2>
      <Grid container spacing={26}>
        <Grid item xs={6}>
          <ElementList />
        </Grid>
        <Grid item xs={6} style={{ textAlign: 'right'}}>
          <VideoComponent videoURL={youtubeVideoURL}/>
        </Grid>
      </Grid>
    </div>
    )
  }
  
