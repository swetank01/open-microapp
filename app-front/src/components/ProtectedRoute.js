// src/components/ProtectedRoute.js
import React from 'react';
import { Router, Routes, Route, useNavigate, Navigate } from 'react-router-dom';

const ProtectedRoute = ({ component: Component, isAuthenticated }) => {
  const navigate = useNavigate(); // Hook to programmatically navigate

  return (
    
    <Routes>
    <Route
      path=''
      element={
        isAuthenticated ? (
          <Component />
        ) : (
          // Redirect to login if not authenticated
          <Navigate to="/login" />
        )
      }
    />
  </Routes>
  );
};

export default ProtectedRoute;
