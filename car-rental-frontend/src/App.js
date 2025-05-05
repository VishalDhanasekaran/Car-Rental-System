import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import HomePage from "./pages/HomePage";
import AddCarPage from "./pages/AddCarPage";
import RentalPage from "./pages/RentalPage";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <Router>
      <div className="container mt-4">
        <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4">
          <Link className="navbar-brand" to="/">Car Rental</Link>
          <div className="collapse navbar-collapse">
            <ul className="navbar-nav mr-auto">
              <li className="nav-item">
                <Link className="nav-link" to="/">Cars</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/add">Add Car</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/rentals">Rentals</Link>
              </li>
            </ul>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/add" element={<AddCarPage />} />
          <Route path="/rentals" element={<RentalPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
