import { useContext, useState } from 'react'
import NavBar from './NavBar'
import Landing from './Landing'
import Training from './Training'
import Practice from './Practice'

import UserContext from "./UserContext";

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import './App.css'

function App() {
  const user = useContext(UserContext);
  let [userState, setUserState] = useState(user);

  return (
    <UserContext.Provider value={{userState,setUserState}}>
      <Router>
        <NavBar/>
          <Routes>
          <Route path="/" element={<Landing/>} />
          <Route path="/training" element={<Training/>} />
          <Route path="/practice" element={<Practice/>} />
          </Routes>
      </Router>
    </UserContext.Provider>
  )
}

export default App
