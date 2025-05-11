-- Create the Fleet Management Database
CREATE DATABASE fleet_management;

-- Use the database
USE fleet_management;

-- Create the Admin table
CREATE TABLE admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password_hash VARCHAR(255) -- Ensure this is hashed securely using bcrypt or argon2
);

-- Create the Users table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    role ENUM('Driver', 'Rider') DEFAULT 'Rider', -- Default role is 'Rider'
    license_number VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
);

-- Create the Vehicles table (consolidating Vehicles and Motorcycles)
CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    type ENUM('Vehicle', 'Motorcycle'), -- Type to differentiate vehicles
    license_plate VARCHAR(50),
    model VARCHAR(100),
    year SMALLINT
);

-- Create the Tracking Logs table
CREATE TABLE tracking_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT, -- Reference to Users table
    vehicle_id INT, -- Reference to Vehicles table
    date_time DATETIME,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Create the Maintenance Schedule table
CREATE TABLE maintenance_schedule (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    vehicle_id INT,
    maintenance_date DATE,
    description TEXT,
    amount DECIMAL(10, 2),
    currency CHAR(3), -- Use reference table for currencies
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Create the Fuel Expenses table
CREATE TABLE fuel_expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    vehicle_id INT,
    date DATE,
    amount DECIMAL(10, 2),
    currency CHAR(3),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Create the Route Optimization table
CREATE TABLE route_optimization (
    optimization_id INT AUTO_INCREMENT PRIMARY KEY,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    optimized_route TEXT
);

-- Create the Route Plan table
CREATE TABLE route_plan (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    vehicle_id INT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Create the Other Expenses table
CREATE TABLE other_expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT,
    amount DECIMAL(10, 2),
    currency CHAR(3),
    date DATE
);

-- Create the Delivery Updates table
CREATE TABLE delivery_updates (
    update_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    vehicle_id INT,
    status VARCHAR(100),
    update_timestamp DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Create the Analytics & Reporting table
CREATE TABLE analytics_reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    report_name VARCHAR(100),
    created_date DATE,
    report_type VARCHAR(50),
    author_id INT,
    description TEXT,
    data BLOB,
    FOREIGN KEY (author_id) REFERENCES admin(admin_id)
);

-- Create the Audit Logs table
CREATE TABLE audit_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    admin_id INT,
    action VARCHAR(255),
    table_name VARCHAR(50),
    record_id INT,
    action_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (admin_id) REFERENCES admin(admin_id)
);

-- Create the Predictions table for AI readiness
CREATE TABLE predictions (
    prediction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    vehicle_id INT,
    prediction_type VARCHAR(50), -- e.g., 'Maintenance', 'Route'
    prediction_result TEXT,
    confidence_score DECIMAL(5, 2), -- AI prediction accuracy
    prediction_date DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

-- Create the Weather Conditions table for weather forecasting
CREATE TABLE weather_conditions (
    weather_id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(255),
    date DATE,
    temperature DECIMAL(5, 2),
    condition VARCHAR(100) -- e.g., 'Rainy', 'Sunny', 'Cloudy'
);

-- Create the User Preferences table for UI optimization
CREATE TABLE user_preferences (
    user_id INT PRIMARY KEY,
    theme ENUM('Light', 'Dark') DEFAULT 'Light',
    notifications_enabled BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create the Localization table for multi-language support
CREATE TABLE localization (
    user_id INT,
    language_code VARCHAR(10),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert example data into the Currencies table
CREATE TABLE currencies (
    currency_code CHAR(3) PRIMARY KEY,
    currency_name VARCHAR(50)
);

INSERT INTO currencies (currency_code, currency_name) VALUES
('USD', 'United States Dollar'),
('Ksh', 'Kenyan Shilling'),
('EUR', 'Euro'),
('GBP', 'British Pound'),
('INR', 'Indian Rupee');

-- Create the Fleet Alerts table for real-time notifications
CREATE TABLE fleet_alerts (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    vehicle_id INT,
    alert_type VARCHAR(50), -- e.g., 'Accident', 'Maintenance Reminder'
    alert_message TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

-- Create the Archived Tracking Logs table for long-term storage
CREATE TABLE archived_tracking_logs (
    log_id INT,
    user_id INT,
    vehicle_id INT,
    date_time DATETIME,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8)
);

-- Add indexes for scalability
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_vehicle_license_plate ON vehicles(license_plate);
CREATE INDEX idx_tracking_logs_date_time ON tracking_logs(date_time);
CREATE INDEX idx_audit_logs_timestamp ON audit_logs(action_timestamp);

-- Insert into admin table
INSERT INTO admin (name, email, password_hash) VALUES
('Techsco', 'admin@example.com', 'hashed_password1');

-- Insert into users table
INSERT INTO users (name, email, phone, role, license_number) VALUES
('John Doe', 'johndoe@example.com', '1234567890', 'Driver', 'AB123456'),
('Jane Smith', 'janesmith@example.com', '0987654321', 'Rider', NULL);

-- Insert into vehicles table
INSERT INTO vehicles (type, license_plate, model, year) VALUES
('Vehicle', 'ABC1234', 'Toyota Corolla', 2020),
('Motorcycle', 'XYZ5678', 'Yamaha R15', 2019);

-- Insert into tracking_logs table
INSERT INTO tracking_logs (user_id, vehicle_id, date_time, latitude, longitude) VALUES
(1, 1, '2025-05-10 10:00:00', 37.7749, -122.4194),
(2, 2, '2025-05-10 12:00:00', 40.7128, -74.0060);

-- Insert into maintenance_schedule table
INSERT INTO maintenance_schedule (user_id, vehicle_id, maintenance_date, description, amount, currency) VALUES
(1, 1, '2025-05-15', 'Oil change', 50.00, 'USD');

-- Insert into fuel_expenses table
INSERT INTO fuel_expenses (user_id, vehicle_id, date, amount, currency) VALUES
(1, 1, '2025-05-09', 30.00, 'USD');

-- Insert into route_optimization table
INSERT INTO route_optimization (start_location, end_location, optimized_route) VALUES
('San Francisco', 'Los Angeles', 'Optimized via I-5');

-- Insert into route_plan table
INSERT INTO route_plan (user_id, vehicle_id, start_date, end_date) VALUES
(1, 1, '2025-05-10', '2025-05-20');

-- Insert into other_expenses table
INSERT INTO other_expenses (description, amount, currency, date) VALUES
('Parking fee', 20.00, 'USD', '2025-05-08');

-- Insert into delivery_updates table
INSERT INTO delivery_updates (user_id, vehicle_id, status, update_timestamp) VALUES
(1, 1, 'Delivered', '2025-05-10 15:00:00');

-- Insert into analytics_reports table
INSERT INTO analytics_reports (report_name, created_date, report_type, author_id, description, data) VALUES
('Monthly Report', '2025-05-01', 'Summary', 1, 'This is a summary report.', NULL);

-- Insert into audit_logs table
INSERT INTO audit_logs (admin_id, action, table_name, record_id) VALUES
(1, 'Insert', 'users', 1);

-- Insert into predictions table
INSERT INTO predictions (user_id, vehicle_id, prediction_type, prediction_result, confidence_score, prediction_date) VALUES
(1, 1, 'Maintenance', 'Change oil', 95.00, '2025-05-09 10:00:00');

-- Insert into weather_conditions table
INSERT INTO weather_conditions (location, date, temperature, condition) VALUES
('San Francisco', '2025-05-10', 18.50, 'Sunny');

-- Insert into user_preferences table
INSERT INTO user_preferences (user_id, theme, notifications_enabled) VALUES
(1, 'Dark', TRUE);

-- Insert into localization table
INSERT INTO localization (user_id, language_code) VALUES
(1, 'en');

-- Insert into fleet_alerts table
INSERT INTO fleet_alerts (user_id, vehicle_id, alert_type, alert_message) VALUES
(1, 1, 'Maintenance Reminder', 'Oil change needed');

-- Insert into archived_tracking_logs table
INSERT INTO archived_tracking_logs (log_id, user_id, vehicle_id, date_time, latitude, longitude) VALUES
(1, 1, 1, '2024-12-31 10:00:00', 37.7749, -122.4194);
