import React, { useState } from 'react';

export default Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // const handleLogin = () => {
  //   // Simulate authentication logic
  //   if (username === 'user' && password === 'password') {
  //     setIsLoggedIn(true);
  //   } else {
  //     alert('Invalid credentials');
  //   }
  // };

  const handleLogin= async () => {
    const url = 'http://localhost:5000/api/login';
    console.log(url);
      try {
        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            // Add any additional headers if needed
          },
          body: JSON.stringify({
            username: 'john',
            password: 'john7',
            // Add your data here
          }),
        });
    
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
    
        const data = await response.json();
        console.log('Response data:', data);
        console.log('Yes')
      } catch (error) {
        console.error('Error:', error.message);
      }
    };

  return (
    <div>
      <h2>Login Page</h2>
      {!isLoggedIn ? (
        <form>
          <label>
            Username:
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </label>
          <br />
          <label>
            Password:
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </label>
          <br />
          <button type="button" onClick={handleLogin}>
            Login
          </button>
        </form>
      ) : (
        <p>Welcome, {username}!</p>
      )}
    </div>
  );
};
