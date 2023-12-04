import React, { useState } from 'react';
import './Style.css'
import ProfileButton from './ProfileButton'
import { NavLink } from 'react-router-dom'; // import the NavLink component


export default function NavBar() {
    const [isSessionActive, setSessionActive] = useState(false);

    const handleLogin = () => {
        // Logic to handle login
        setSessionActive(true);
    };

    const handleLogout = () => {
        // Logic to handle logout
        setSessionActive(false);
    };
    return (
        
        <nav className='navigation'>
            <NavLink to="/" className={({isActive})=>isActive?" active":""}>Home</NavLink>

            {isSessionActive ? (
                <div>
                    <NavLink to="/training" className={({isActive})=>isActive?" active":""}>Training</NavLink>
                    <NavLink to="/practice" className={({isActive})=>isActive?" active":""}>Practice</NavLink>
                    <div className='right'>
                        <ProfileButton/>
                    </div>
                </div>
            ):(
                <div>
                    <div className='right'>
                        <button onClick={handleLogin}>Login</button>
                    </div>
                    
                </div>
            )}
           

        </nav>
        
    );

}