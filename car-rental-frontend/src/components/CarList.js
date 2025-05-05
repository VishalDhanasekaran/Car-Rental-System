import React, { useState, useEffect } from 'react';
import { Table, Button, Badge, Container, Row, Col, Spinner } from 'react-bootstrap';
import API from '../services/api';
import RentCarModel from './RentCarModel';

const CarList = () => {
  const [cars, setCars] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showRentModal, setShowRentModal] = useState(false);
  const [selectedCar, setSelectedCar] = useState(null);

  // Fetch cars when component mounts
  useEffect(() => {
    fetchCars();
  }, []);

  const fetchCars = async () => {
    try {
      setLoading(true);
      const carsData = await API.getCars();
      setCars(carsData);
      setError(null);
    } catch (err) {
      setError('Error loading cars. Please try again.');
      console.error('Error fetching cars:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleRentClick = (car) => {
    setSelectedCar(car);
    setShowRentModal(true);
  };

  const handleRentSuccess = () => {
    setShowRentModal(false);
    fetchCars(); // Refresh car list after successful rental
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

  if (error) {
    return (
      <Container className="mt-5">
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      </Container>
    );
  }

  return (
    <Container className="mt-4">
      <h2>Available Cars</h2>
      <Row className="mb-3">
        <Col>
          <Button variant="primary" onClick={fetchCars}>
            Refresh List
          </Button>
        </Col>
      </Row>
      
      {cars.length === 0 ? (
        <div className="alert alert-info">No cars available.</div>
      ) : (
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Make</th>
              <th>Model</th>
              <th>Year</th>
              <th>Daily Rate</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {cars.map((car) => (
              <tr key={car.id}>
                <td>{car.make}</td>
                <td>{car.model}</td>
                <td>{car.year}</td>
                <td>${car.daily_rate.toFixed(2)}</td>
                <td>
                  {car.available ? (
                    <Badge bg="success">Available</Badge>
                  ) : (
                    <Badge bg="danger">Rented</Badge>
                  )}
                </td>
                <td>
                  <Button
                    variant="primary"
                    size="sm"
                    disabled={!car.available}
                    onClick={() => handleRentClick(car)}
                  >
                    Rent
                  </Button>
                </td>
              </tr>
            ))}
          </tbody>
        </Table>
      )}

      {selectedCar && (
        <RentCarModel
          show={showRentModal}
          onHide={() => setShowRentModal(false)}
          car={selectedCar}
          onSuccess={handleRentSuccess}
        />
      )}
    </Container>
  );
};

export default CarList;