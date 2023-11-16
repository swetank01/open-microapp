import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import './App.css';
import Home from './components/Home';
import ProtectedRoute from './components/ProtectedRoute';
import Dashboard from './components/Dashboard';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/login" element={<Home isAuthenticated={isAuthenticated} setIsAuthenticated={setIsAuthenticated} />} />
          <Route path="/dashboard/*" element={<ProtectedRoute component={Dashboard} isAuthenticated={isAuthenticated} />} />
          <Route path="/" element={<Navigate to="/login" />} />
          
        </Routes>
      </Router>
    </div>
  );
}

export default App;
