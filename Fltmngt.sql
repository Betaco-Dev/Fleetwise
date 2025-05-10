-- Create the Fleet Management Database
CREATE DATABASE FleetManagement;

-- Use the database
USE FleetManagement;

-- Create the Admin table
CREATE TABLE Admin (
    AdminID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    PasswordHash VARCHAR(255)
);

-- Create the Users table (for both drivers and riders)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Role ENUM('Driver', 'Rider'), -- Role can be 'Driver' or 'Rider'
    LicenseNumber VARCHAR(50) -- License number applies to both roles
);

-- Create the Vehicles table
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,
    VehicleType VARCHAR(50),
    LicensePlate VARCHAR(50),
    Model VARCHAR(100),
    Year INT
);

-- Create the Motorcycles table
CREATE TABLE Motorcycles (
    MotorcycleID INT AUTO_INCREMENT PRIMARY KEY,
    LicensePlate VARCHAR(50),
    Model VARCHAR(100),
    Year INT
);

-- Create the Tracking Logs table
CREATE TABLE TrackingLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT, -- Reference to Users table for both drivers and riders
    VehicleID INT NULL, -- Reference to Vehicles table
    MotorcycleID INT NULL, -- Reference to Motorcycles table
    DateTime DATETIME,
    Latitude DECIMAL(10, 8),
    Longitude DECIMAL(11, 8),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID),
    FOREIGN KEY (MotorcycleID) REFERENCES Motorcycles(MotorcycleID)
);

-- Create the Maintenance Schedule table
CREATE TABLE MaintenanceSchedule (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT, -- Reference to Users table for both drivers and riders
    VehicleID INT NULL, -- Reference to Vehicles table
    MotorcycleID INT NULL, -- Reference to Motorcycles table
    MaintenanceDate DATE,
    Description TEXT,
    Amount DECIMAL(10, 2), -- Maintenance cost
    Currency ENUM('Ksh', 'USD', 'EUR', 'GBP', 'INR') DEFAULT 'USD', -- Currency column
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID),
    FOREIGN KEY (MotorcycleID) REFERENCES Motorcycles(MotorcycleID)
);

-- Create the Fuel Expenses table
CREATE TABLE FuelExpenses (
    ExpenseID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT, -- Reference to Users table for both drivers and riders
    VehicleID INT NULL, -- Reference to Vehicles table
    MotorcycleID INT NULL, -- Reference to Motorcycles table
    Date DATE,
    Amount DECIMAL(10, 2),
    Currency ENUM('Ksh', 'USD', 'EUR', 'GBP', 'INR') DEFAULT 'USD', -- Currency column
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID),
    FOREIGN KEY (MotorcycleID) REFERENCES Motorcycles(MotorcycleID)
);

-- Create the Route Optimization table
CREATE TABLE RouteOptimization (
    OptimizationID INT AUTO_INCREMENT PRIMARY KEY,
    StartLocation VARCHAR(255),
    EndLocation VARCHAR(255),
    OptimizedRoute TEXT
);

-- Create the Route Plan table
CREATE TABLE RoutePlan (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT, -- Reference to Users table for both drivers and riders
    VehicleID INT NULL, -- Reference to Vehicles table
    MotorcycleID INT NULL, -- Reference to Motorcycles table
    StartDate DATE,
    EndDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID),
    FOREIGN KEY (MotorcycleID) REFERENCES Motorcycles(MotorcycleID)
);

-- Create the Other Expenses table
CREATE TABLE OtherExpenses (
    ExpenseID INT AUTO_INCREMENT PRIMARY KEY,
    Description TEXT,
    Amount DECIMAL(10, 2),
    Currency ENUM('Ksh', 'USD', 'EUR', 'GBP', 'INR') DEFAULT 'USD', -- Currency column
    Date DATE
);

-- Create the Delivery Updates table
CREATE TABLE DeliveryUpdates (
    UpdateID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT, -- Reference to Users table for both drivers and riders
    VehicleID INT NULL, -- Reference to Vehicles table
    MotorcycleID INT NULL, -- Reference to Motorcycles table
    Status VARCHAR(100),
    UpdateTimestamp DATETIME,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID),
    FOREIGN KEY (MotorcycleID) REFERENCES Motorcycles(MotorcycleID)
);

-- Create the Analytics & Reporting table
CREATE TABLE AnalyticsReports (
    ReportID INT AUTO_INCREMENT PRIMARY KEY,
    ReportName VARCHAR(100),
    CreatedDate DATE,
    Data BLOB
);

-- Insert example data into each table
-- Admin
INSERT INTO Admin (Name, Email, PasswordHash) VALUES
('John Doe', 'john.doe@example.com', 'hashed_password');

-- Users
INSERT INTO Users (Name, Email, Phone, Role, LicenseNumber) VALUES
('Alice Smith', 'alice.smith@example.com', '123-456-7890', 'Driver', 'DL123456'),
('Bob Johnson', 'bob.johnson@example.com', '987-654-3210', 'Rider', 'RL654321');

-- Vehicles
INSERT INTO Vehicles (VehicleType, LicensePlate, Model, Year) VALUES
('Truck', 'ABC123', 'Ford F-150', 2020);

-- Motorcycles
INSERT INTO Motorcycles (LicensePlate, Model, Year) VALUES
('MOTO456', 'Yamaha YZF-R3', 2019);

-- Tracking Logs
INSERT INTO TrackingLogs (UserID, VehicleID, MotorcycleID, DateTime, Latitude, Longitude) VALUES
(1, 1, NULL, '2025-05-10 06:00:00', 37.7749, -122.4194);

-- Maintenance Schedule
INSERT INTO MaintenanceSchedule (UserID, VehicleID, MotorcycleID, MaintenanceDate, Description, Amount, Currency) VALUES
(1, 1, NULL, '2025-06-01', 'Oil change and tire rotation', 150.00, 'USD'),
(2, NULL, 1, '2025-06-01', 'Brake pad replacement', 12000.00, 'Ksh');

-- Fuel Expenses
INSERT INTO FuelExpenses (UserID, VehicleID, MotorcycleID, Date, Amount, Currency) VALUES
(1, 1, NULL, '2025-05-09', 50.75, 'USD'),
(2, NULL, 1, '2025-05-09', 6000.00, 'Ksh');

-- Route Optimization
INSERT INTO RouteOptimization (StartLocation, EndLocation, OptimizedRoute) VALUES
('San Francisco', 'Los Angeles', 'Optimized Route Data Here');

-- Route Plan
INSERT INTO RoutePlan (UserID, VehicleID, MotorcycleID, StartDate, EndDate) VALUES
(1, 1, NULL, '2025-05-10', '2025-05-15');

-- Other Expenses
INSERT INTO OtherExpenses (Description, Amount, Currency, Date) VALUES
('Toll fees', 25.00, 'USD', '2025-05-09'),
('Parking fees', 500.00, 'Ksh', '2025-05-09');

-- Delivery Updates
INSERT INTO DeliveryUpdates (UserID, VehicleID, MotorcycleID, Status, UpdateTimestamp) VALUES
(2, NULL, 1, 'Delivered', '2025-05-10 06:15:00');

-- Analytics & Reporting
INSERT INTO AnalyticsReports (ReportName, CreatedDate, Data) VALUES
('Monthly Fuel Usage', '2025-05-01', NULL);
