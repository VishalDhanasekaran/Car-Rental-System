import React, { useState } from 'react';
import { Modal, Button, Form, Alert } from 'react-bootstrap';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import API from '../services/api';

const RentCarModel = ({ show, onHide, car, onSuccess }) => {
  const [userName, setUserName] = useState('');
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date(new Date().setDate(new Date().getDate() + 3)));
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    // Basic validation
    if (!userName.trim()) {
      setError('Please enter your name');
      return;
    }

    if (startDate >= endDate) {
      setError('End date must be after start date');
      return;
    }

    try {
      setIsSubmitting(true);
      await API.rentCar(car.id, {
        car_id: car.id,
        user_name: userName,
        start_date: startDate.toISOString(),
        end_date: endDate.toISOString()
      });
      
      setIsSubmitting(false);
      onSuccess();
    } catch (err) {
      setIsSubmitting(false);
      if (err.response && err.response.data && err.response.data.detail) {
        setError(err.response.data.detail);
      } else {
        setError('Error renting car. Please try again.');
      }
      console.error('Error renting car:', err);
    }
  };

  return (
    <Modal show={show} onHide={onHide} centered>
      <Modal.Header closeButton>
        <Modal.Title>Rent {car?.make} {car?.model}</Modal.Title>
      </Modal.Header>
      <Form onSubmit={handleSubmit}>
        <Modal.Body>
          {error && <Alert variant="danger">{error}</Alert>}
          
          <div className="mb-3">
            <p>
              <strong>Car Details:</strong> {car?.year} {car?.make} {car?.model}
            </p>
            <p>
              <strong>Daily Rate:</strong> ${car?.daily_rate.toFixed(2)}
            </p>
          </div>

          <Form.Group className="mb-3">
            <Form.Label>Your Name</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter your full name"
              value={userName}
              onChange={(e) => setUserName(e.target.value)}
              required
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Start Date</Form.Label>
            <br />
            <DatePicker
              selected={startDate}
              onChange={(date) => setStartDate(date)}
              minDate={new Date()}
              className="form-control"
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>End Date</Form.Label>
            <br />
            <DatePicker
              selected={endDate}
              onChange={(date) => setEndDate(date)}
              minDate={new Date(startDate.getTime() + 86400000)} // day after start date
              className="form-control"
            />
          </Form.Group>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={onHide}>
            Cancel
          </Button>
          <Button variant="primary" type="submit" disabled={isSubmitting}>
            {isSubmitting ? 'Processing...' : 'Rent Now'}
          </Button>
        </Modal.Footer>
      </Form>
    </Modal>
  );
};

export default RentCarModel;