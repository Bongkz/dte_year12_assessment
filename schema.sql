-- 1. Create the Customer table
CREATE TABLE Customer (
    ID INTEGER PRIMARY KEY,
    First_Name TEXT,
    Surname TEXT,
    Address TEXT
);

-- 2. Create the Menu table
CREATE TABLE Menu (
    ID INTEGER PRIMARY KEY,
    Food_Name TEXT,
    Price INTEGER
);

-- 3. Create the Order table (Depends on Customer)
CREATE TABLE "Order" (
    ID INTEGER PRIMARY KEY,
    Customer_ID INTEGER,
    Order_Date TEXT,
    Subtotal INTEGER,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(ID)
);

-- 4. Create the ItemsPurchased table (Depends on Order and Menu)
CREATE TABLE ItemsPurchased (
    ID INTEGER PRIMARY KEY,
    Order_ID INTEGER,
    Menu_ID INTEGER,
    Quantity INTEGER,
    FOREIGN KEY (Order_ID) REFERENCES "Order"(ID),
    FOREIGN KEY (Menu_ID) REFERENCES Menu(ID)
);