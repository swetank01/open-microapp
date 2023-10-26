// src/components/LoginForm.js
import React, { useState } from 'react';
import axios from 'axios';

const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      console.log('Login button clicked'); // Check if the function is triggered
      const response = await axios.post('http://localhost:5000/login', {
        username: username,
        password: password
      });
      
      const { access_token } = response.data;
      console.log('Login successful:', response.data); // Log the response data
      
      // Store the token and implement further logic (e.g., redirect to dashboard)
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  return (
    <div className="form">
      <h2>Login</h2>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
             <br />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
            <br />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default LoginForm;
