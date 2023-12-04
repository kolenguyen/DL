import { useContext, useState } from 'react'
import axios from "axios"
import NavBar from './NavBar'
import Footer from './Footer'
import Landing from './Landing'
import Training from './Training'
import Practice from './Practice'
import Results from './Results'
import {createTheme, ThemeProvider} from '@mui/material/styles'

import UserContext from "./UserContext";

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import './App.css'
import LoginPage from './LoginPage'
import Profile from './Profile'

const theme = createTheme();

function App() {
  const user = useContext(UserContext);
  let [userState, setUserState] = useState(user);

  return (
   <ThemeProvider theme={theme}>
    <UserContext.Provider value={{userState,setUserState}}>
      <Router>
        <NavBar/>
          <Routes>
          <Route path="/" element={<Landing/>} />
          <Route path="/training" element={<Training/>} />
          <Route path="/practice" element={<Practice/>} />
          <Route path="/login" element={<LoginPage/>} />
          <Route path="/profile" element={<Profile/>} />
          <Route path="/results" element={<Results/>} />
          </Routes>
      </Router>
      <Footer/>

    </UserContext.Provider>
    </ThemeProvider>
  )
}

export default App
