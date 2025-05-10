-- Create the Fleet Management Database
CREATE DATABASE fleet_management;

-- Use the database
USE fleet_management;

-- Create the Admin table
CREATE TABLE admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password_hash VARCHAR(255) -- Ensure this is hashed securely
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
    data BLOB
);

-- Insert example data into the currencies table
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
