// src/components/Home.js
import React from 'react';
import LoginForm from './LoginForm';
import RegistrationForm from './RegistrationForm';

const Home = (props) => {
  return (
    <div className="home">
      <h1>Welcome to Microservices App</h1>
      <div className="forms">
        <LoginForm mohit={props} />
        <RegistrationForm />
      </div>
    </div>
  );
};

export default Home;
