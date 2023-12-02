
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
            <h2>ASL TRANSLATOR</h2>
            <h3>Translate and learn ASL language.</h3>
            {/* <ul>
                <li>Group 2</li>
                <li>Members:</li>
                <li>Build using React, MUI and python</li>
            </ul> */}

            <ul>
                <p>Deep learning project using Python, Flask and React</p>
                <p>Made by Kole, Fernando, Yashi and Arjun</p>
            </ul>

            <Button variant="contained" href='/login'>Login</Button>      
            {/* <Button variant="contained" path="/practice" element={<Practice/>}>Register</Button>     */}
            </header>
    </main>
      </div>
    )
  }
  
