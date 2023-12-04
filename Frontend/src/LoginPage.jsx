import React, { useState } from 'react';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import LoginForm from './LoginForm';
import Grid from '@mui/material/Grid'; // Import Grid to center the form
import Paper from '@mui/material/Paper'; // Import Paper for the background square

const LoginPage = () => {
  const [loginError, setLoginError] = useState('');

  const handleLogin = async (credentials) => {
    try {
      console.log(credentials)
      // Simulate a request to the server for authentication
      // this is from port 5000 not 3000
      const response = await fetch('http://127.0.0.1:5000/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials),
      });

      if (!response.ok) {
        throw new Error('Invalid credentials');
      }

      // If authentication is successful, you can redirect or perform other actions
      console.log('Login successful!');
      setLoginError('');
      //did not work
      history.push('/training');
    } catch (error) {
      // Handle authentication error
      console.error('Authentication error:', error.message);
      setLoginError('Invalid username or password');
    }
  };

  return (
    <Container component="main" maxWidth="xs">
      <Paper elevation={3} style={{ padding: 20, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Grid container justifyContent="center">
          <Typography variant="h5" align="center" gutterBottom>
            Login
          </Typography>
        </Grid>
        <LoginForm handleLogin={handleLogin} loginError={loginError} />
      </Paper>

    </Container>
  );
};

export default LoginPage;