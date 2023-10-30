// src/components/ProtectedRoute.js
import React from 'react';
import { Router, Routes, Route, useNavigate } from 'react-router-dom';

const ProtectedRoute = ({ component: Component, isAuthenticated, ...rest }) => {
  const navigate = useNavigate(); // Hook to programmatically navigate

  return (
    <Routes>
    <Route
      {...rest}
      element={
        isAuthenticated ? (
          <Component />
        ) : (
          // Redirect to login if not authenticated
          navigate('/login')
        )
      }
    />
  </Routes>
  );
};

export default ProtectedRoute;
