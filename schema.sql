-- ==========================================================
-- DATABASE SCHEMA: Restaurant System
-- Derived from ERD: Customer, Order, Menu, ItemsPurchased
-- ==========================================================

-- 1. Cleanup: Remove existing tables to allow for re-runs
DROP TABLE IF EXISTS ItemsPurchased;
DROP TABLE IF EXISTS Customer_Order;
DROP TABLE IF EXISTS Menu;
DROP TABLE IF EXISTS Customer;

-- 2. Create Customer Table
-- Stores personal details of people placing orders
CREATE TABLE Customer (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_Name TEXT NOT NULL,
    Surname TEXT NOT NULL,
    Address TEXT
);

-- 3. Create Menu Table
-- Stores the food items and their prices
CREATE TABLE Menu (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Food_Name TEXT NOT NULL,
    Price INTEGER NOT NULL -- Stored as whole numbers (e.g., 15 for $15)
);

-- 4. Create Customer_Order Table
-- Links a specific order to a Customer
CREATE TABLE Customer_Order (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Customer_ID INTEGER,
    Order_Date TEXT DEFAULT CURRENT_DATE,
    Subtotal INTEGER,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(ID) ON DELETE CASCADE
);

-- 5. Create ItemsPurchased Table
-- The "Bridge" table connecting Orders to Menu items (Many-to-Many)
CREATE TABLE ItemsPurchased (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Order_ID INTEGER,
    Menu_ID INTEGER,
    Quantity INTEGER DEFAULT 1,
    FOREIGN KEY (Order_ID) REFERENCES Customer_Order(ID) ON DELETE CASCADE,
    FOREIGN KEY (Menu_ID) REFERENCES Menu(ID) ON DELETE CASCADE
);

-- ==========================================================
-- TEST DATA: Insert some initial rows to verify setup
-- ==========================================================

INSERT INTO Customer (First_Name, Surname, Address) 
VALUES ('John', 'Doe', '123 Tech Way');

INSERT INTO Menu (Food_Name, Price) 
VALUES ('Classic Burger', 12), ('Large Fries', 5), ('Soda', 3);

INSERT INTO Customer_Order (Customer_ID, Order_Date, Subtotal) 
VALUES (1, '2026-03-18', 17);

-- John Doe ordered 1 Burger and 1 Fry
INSERT INTO ItemsPurchased (Order_ID, Menu_ID, Quantity) 
VALUES (1, 1, 1), (1, 2, 1);