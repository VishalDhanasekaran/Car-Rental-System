import React, { useState } from 'react';
import { Form, Button, Container, Row, Col, Alert } from 'react-bootstrap';
import API from '../services/api';

const AddCarForm = ({ onCarAdded }) => {
  const [carData, setCarData] = useState({
    make: '',
    model: '',
    year: new Date().getFullYear(),
    daily_rate: ''
  });
  
  const [errors, setErrors] = useState({});
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState({ message: '', type: '' });

  const validateForm = () => {
    const newErrors = {};
    
    if (!carData.make.trim()) {
      newErrors.make = 'Make is required';
    }
    
    if (!carData.model.trim()) {
      newErrors.model = 'Model is required';
    }
    
    const yearNum = parseInt(carData.year);
    if (isNaN(yearNum) || yearNum < 1900 || yearNum > new Date().getFullYear() + 1) {
      newErrors.year = `Year must be between 1900 and ${new Date().getFullYear() + 1}`;
    }
    
    const rateNum = parseFloat(carData.daily_rate);
    if (isNaN(rateNum) || rateNum <= 0) {
      newErrors.daily_rate = 'Daily rate must be a positive number';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCarData({
      ...carData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }
    
    try {
      setSubmitting(true);
      
      // Convert string values to appropriate types
      const formattedData = {
        ...carData,
        year: parseInt(carData.year),
        daily_rate: parseFloat(carData.daily_rate)
      };
      
      await API.addCar(formattedData);
      
      // Clear form
      setCarData({
        make: '',
        model: '',
        year: new Date().getFullYear(),
        daily_rate: ''
      });
      
      setResult({
        message: 'Car added successfully!',
        type: 'success'
      });
      
      // Call the callback if provided
      if (onCarAdded) {
        onCarAdded();
      }
      
      // Clear success message after 5 seconds
      setTimeout(() => setResult({ message: '', type: '' }), 5000);
    } catch (err) {
      console.error('Error adding car:', err);
      
      let errorMessage = 'Failed to add car. Please try again.';
      if (err.response && err.response.data && err.response.data.detail) {
        errorMessage = err.response.data.detail;
      }
      
      setResult({
        message: errorMessage,
        type: 'danger'
      });
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <Container className="mt-4">
      <h2>Add New Car</h2>
      
      {result.message && (
        <Alert variant={result.type} className="mt-3">
          {result.message}
        </Alert>
      )}
      
      <Form onSubmit={handleSubmit}>
        <Row>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Make</Form.Label>
              <Form.Control
                type="text"
                name="make"
                value={carData.make}
                onChange={handleChange}
                isInvalid={!!errors.make}
                placeholder="e.g., Toyota"
              />
              <Form.Control.Feedback type="invalid">
                {errors.make}
              </Form.Control.Feedback>
            </Form.Group>
          </Col>
          
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Model</Form.Label>
              <Form.Control
                type="text"
                name="model"
                value={carData.model}
                onChange={handleChange}
                isInvalid={!!errors.model}
                placeholder="e.g., Camry"
              />
              <Form.Control.Feedback type="invalid">
                {errors.model}
              </Form.Control.Feedback>
            </Form.Group>
          </Col>
        </Row>
        
        <Row>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Year</Form.Label>
              <Form.Control
                type="number"
                name="year"
                value={carData.year}
                onChange={handleChange}
                isInvalid={!!errors.year}
                min="1900"
                max={new Date().getFullYear() + 1}
              />
              <Form.Control.Feedback type="invalid">
                {errors.year}
              </Form.Control.Feedback>
            </Form.Group>
          </Col>
          
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Daily Rate ($)</Form.Label>
              <Form.Control
                type="number"
                name="daily_rate"
                value={carData.daily_rate}
                onChange={handleChange}
                isInvalid={!!errors.daily_rate}
                step="0.01"
                min="0.01"
                placeholder="e.g., 49.99"
              />
              <Form.Control.Feedback type="invalid">
                {errors.daily_rate}
              </Form.Control.Feedback>
            </Form.Group>
          </Col>
        </Row>
        
        <Button variant="primary" type="submit" disabled={submitting}>
          {submitting ? 'Adding...' : 'Add Car'}
        </Button>
      </Form>
    </Container>
  );
};

export default AddCarForm;