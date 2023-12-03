
import './Style.css'
import Button from '@mui/material/Button';

export default function Landing() {  
    return (
    <div style={{margin: 0}}>
    <main className="landing">
        <video src="https://assets.mixkit.co/videos/preview/mixkit-two-women-chatting-with-sign-language-4571-large.mp4" 
        muted loop autoPlay>
        </video>
        <header className="landingtext">
            <h2>ASL Translator</h2>
            <h3>Translate and learn ASL language.</h3>
            <Button variant="contained" href='/login'>Login</Button>        
            </header>
    </main>
      </div>
    )
  }
  
