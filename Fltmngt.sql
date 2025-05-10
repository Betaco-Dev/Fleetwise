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
