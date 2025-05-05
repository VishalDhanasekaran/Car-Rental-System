import axios from 'axios';

const API_URL = 'http://localhost:8000';

// API service for interacting with backend
const API = {
  // Car operations
  getCars: async () => {
    try {
      const response = await axios.get(`${API_URL}/cars/`);
      return response.data;
    } catch (error) {
      console.error('Error fetching cars:', error);
      throw error;
    }
  },

  getCar: async (carId) => {
    try {
      const response = await axios.get(`${API_URL}/cars/${carId}`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching car ${carId}:`, error);
      throw error;
    }
  },

  addCar: async (carData) => {
    try {
      const response = await axios.post(`${API_URL}/cars/`, carData);
      return response.data;
    } catch (error) {
      console.error('Error adding car:', error);
      throw error;
    }
  },

  // Rental operations
  getRentals: async () => {
    try {
      const response = await axios.get(`${API_URL}/rentals/`);
      return response.data;
    } catch (error) {
      console.error('Error fetching rentals:', error);
      throw error;
    }
  },

  getRental: async (rentalId) => {
    try {
      const response = await axios.get(`${API_URL}/rentals/${rentalId}`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching rental ${rentalId}:`, error);
      throw error;
    }
  },

  rentCar: async (carId, rentalData) => {
    try {
      const response = await axios.post(`${API_URL}/cars/${carId}/rent`, rentalData);
      return response.data;
    } catch (error) {
      console.error(`Error renting car ${carId}:`, error);
      throw error;
    }
  },

  cancelRental: async (rentalId) => {
    try {
      await axios.delete(`${API_URL}/rentals/${rentalId}`);
      return true;
    } catch (error) {
      console.error(`Error canceling rental ${rentalId}:`, error);
      throw error;
    }
  }
};

export default API;