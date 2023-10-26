// src/components/RegistrationForm.js
import React, { useState } from 'react';
import axios from 'axios';

const RegistrationForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleRegistration = async () => {
    try {
      console.log('Registration button clicked'); // Check if the function is triggered
      const response = await axios.post('http://localhost:5000/register', {
        username: username,
        password: password
      });
      console.log('Registration successful:', response.data); // Log the response data
      // Implement further logic (e.g., show success message, redirect to login)
    } catch (error) {
      console.error('Registration failed:', error);
    }
  };

  return (
    <div className="form">
      <h2>Registration</h2>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleRegistration}>Register</button>
    </div>
  );
};

export default RegistrationForm;
