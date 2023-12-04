import React from 'react';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import LoginForm from './LoginForm';
import Grid from '@mui/material/Grid'; // Import Grid to center the form
import Paper from '@mui/material/Paper'; // Import Paper for the background square

const LoginPage = () => {
  const handleLogin = (credentials) => {
    // Handle authentication logic here (e.g., send a request to the server)
    console.log('Login credentials:', credentials);
  };

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