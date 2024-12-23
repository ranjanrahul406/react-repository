import React from 'react';
import { Link } from 'react-router-dom'; // Optional, if using React Router

const Navbar = () => {
  return (
    <nav className="bg-gray-800 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex-shrink-0 text-xl font-bold">
            <Link to="/">Education Platform</Link>
          </div>
          <div className="hidden md:flex space-x-4">
            <Link to="/" className="hover:text-gray-300">Home</Link>
            <Link to="/Standard" className="hover:text-gray-300">Standard</Link>
            <Link to="/Subjects" className="hover:text-gray-300">Subjects</Link>
            <Link to="/Lectures" className="hover:text-gray-300">Lectures</Link>            
            <Link to="/Labs" className="hover:text-gray-300">Labs</Link>
            <Link to="/TestYourSkills" className="hover:text-gray-300">Test your skills</Link>
            <Link to="/AnyDoubt" className="hover:text-gray-300">Any doubt</Link>
            
            
            
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
