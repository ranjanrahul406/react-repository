import React from "react";
import Navbar from "./pages/components/Navbar";
import {BrowserRouter as Router, Routes, Route } from 'react-router-dom';
//import LoginPage from "./pages/LoginPage";
import Home from "./pages/Home";
import AnyDoubt from "./pages/AnyDoubt";
import Labs from "./pages/Labs";
import Lectures from "./pages/Lectures";
import Standard from "./pages/Standard";
import Subjects from "./pages/Subjects";
import TestYourSkills from "./pages/TestYourSkills";

function App() {

  return (

    <Router>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/Standard" element={<Standard/>} />
        <Route path="/Subjects" element={<Subjects/>} />
        <Route path="/Lectures" element={<Lectures/>} />
        <Route path="/Labs" element={<Labs/>} />
        <Route path="/TestYourSkills" element={<TestYourSkills/>} />
        <Route path="/AnyDoubt" element={<AnyDoubt/>} />
      </Routes>
    </Router>

    );
};

export default App
