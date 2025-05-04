-- Insert sample cars
INSERT INTO cars (make, model, year, daily_rate, available)
VALUES
  ('Toyota', 'Camry', 2023, 50.00, 1),
  ('Honda', 'Civic', 2022, 45.00, 1),
  ('Ford', 'Mustang', 2023, 75.00, 1),
  ('Chevrolet', 'Malibu', 2021, 48.00, 1),
  ('Nissan', 'Altima', 2022, 47.00, 1),
  ('Hyundai', 'Elantra', 2023, 42.00, 1),
  ('Kia', 'Forte', 2022, 40.00, 1),
  ('BMW', 'X3', 2021, 85.00, 1),
  ('Mercedes-Benz', 'C-Class', 2022, 90.00, 1),
  ('Audi', 'A4', 2023, 88.00, 1);

-- Insert some sample rentals (one active, one past)
INSERT INTO rentals (car_id, user_name, start_date, end_date, rental_date)
VALUES
  (
    3, 'John Smith',
    datetime('now', '-5 days'),
    datetime('now', '+2 days'),
    datetime('now', '-5 days')
  ),
  (
    5, 'Jane Doe',
    datetime('now', '-10 days'),
    datetime('now', '-5 days'),
    datetime('now', '-10 days')
  );

-- Update availability for cars with active rentals
UPDATE cars
SET available = 0
WHERE id IN (
  SELECT car_id 
  FROM rentals 
  WHERE end_date > datetime('now')
);