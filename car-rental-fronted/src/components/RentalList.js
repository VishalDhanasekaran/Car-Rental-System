import React, { useState, useEffect } from 'react';
import { Table, Button, Container, Spinner, Alert } from 'react-bootstrap';
import API from '../services/api';

const RentalsList = () => {
  const [rentals, setRentals] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [cancelResult, setCancelResult] = useState({ message: '', type: '' });

  // Load rentals when component mounts
  useEffect(() => {
    fetchRentals();
  }, []);

  const fetchRentals = async () => {
    try {
      setLoading(true);
      const rentalsData = await API.getRentals();
      setRentals(rentalsData);
      setError(null);
    } catch (err) {
      setError('Error loading rentals. Please try again.');
      console.error('Error fetching rentals:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCancelRental = async (rentalId) => {
    if (!window.confirm('Are you sure you want to cancel this rental?')) {
      return;
    }

    try {
      await API.cancelRental(rentalId);
      // Filter out the canceled rental
      setRentals(rentals.filter(rental => rental.id !== rentalId));
      setCancelResult({
        message: 'Rental canceled successfully!',
        type: 'success'
      });
      setTimeout(() => setCancelResult({ message: '', type: '' }), 5000);
    } catch (err) {
      console.error('Error canceling rental:', err);
      let errorMessage = 'Failed to cancel rental. Please try again.';
      
      if (err.response && err.response.data && err.response.data.detail) {
        errorMessage = err.response.data.detail;
      }
      
      setCancelResult({
        message: errorMessage,
        type: 'danger'
      });
      setTimeout(() => setCancelResult({ message: '', type: '' }), 5000);
    }
  };

  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };

  if (loading) {
    return (
      <Container className="text-center mt-5">
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
      </Container>
    );
  }

  return (
    <Container className="mt-4">
      <h2>My Rentals</h2>
      
      {cancelResult.message && (
        <Alert variant={cancelResult.type} className="mt-3">
          {cancelResult.message}
        </Alert>
      )}
      
      {error && (
        <Alert variant="danger" className="mt-3">
          {error}
        </Alert>
      )}
      
      <Button 
        variant="outline-primary" 
        className="mb-3 mt-2"
        onClick={fetchRentals}
      >
        Refresh List
      </Button>
      
      {rentals.length === 0 ? (
        <Alert variant="info">No active rentals found.</Alert>
      ) : (
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Rental ID</th>
              <th>Car ID</th>
              <th>User Name</th>
              <th>Start Date</th>
              <th>End Date</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {rentals.map((rental) => {
              const now = new Date();
              const endDate = new Date(rental.end_date);
              const isActive = endDate >= now;
              
              return (
                <tr key={rental.id}>
                  <td>{rental.id}</td>
                  <td>{rental.car_id}</td>
                  <td>{rental.user_name}</td>
                  <td>{formatDate(rental.start_date)}</td>
                  <td>{formatDate(rental.end_date)}</td>
                  <td>
                    {isActive ? (
                      <span className="text-success">Active</span>
                    ) : (
                      <span className="text-secondary">Completed</span>
                    )}
                  </td>
                  <td>
                    <Button
                      variant="danger"
                      size="sm"
                      onClick={() => handleCancelRental(rental.id)}
                      disabled={!isActive}
                    >
                      Cancel
                    </Button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </Table>
      )}
    </Container>
  );
};

export default RentalsList;