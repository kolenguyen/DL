import React from 'react';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import LoginForm from './LoginForm';
import Grid from '@mui/material/Grid'; // Import Grid to center the form
import Paper from '@mui/material/Paper'; // Import Paper for the background square

const LoginPage = () => {
  const handleLogin = async(credentials) => {
    // Handle authentication logic here (e.g., send a request to the server)
    console.log('Login credentials:', credentials);
    const url = 'http://127.0.0.1:5000/auth/login';
    console.log(url);
      try {
        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            // Add any additional headers if needed
          },
          body: JSON.stringify({
            username: 'john7',
            password: 'john',
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
  }
  
  // const handleLogin= async () => {
  //   const url = 'http://localhost:5000/api/login';
  //   console.log(url);
  //     try {
  //       const response = await fetch(url, {
  //         method: 'POST',
  //         headers: {
  //           'Content-Type': 'application/json',
  //           // Add any additional headers if needed
  //         },
  //         body: JSON.stringify({
  //           username: 'john',
  //           password: 'john7',
  //           // Add your data here
  //         }),
  //       });
    
  //       if (!response.ok) {
  //         throw new Error('Network response was not ok');
  //       }
    
  //       const data = await response.json();
  //       console.log('Response data:', data);
  //       console.log('Yes')
  //     } catch (error) {
  //       console.error('Error:', error.message);
  //     }
  //   };;

  

  return (
    <Container component="main" maxWidth="xs">
      <Paper elevation={3} style={{ padding: 20, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Grid container justifyContent="center">
          <Typography variant="h5" align="center" gutterBottom>
            Login
          </Typography>
        </Grid>
        <LoginForm handleLogin={handleLogin} />
      </Paper>

    </Container>
  );
};

export default LoginPage;