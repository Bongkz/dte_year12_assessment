CREATE TABLE Menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT
);

CREATE TABLE Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    address TEXT,
    items_ordered TEXT, -- A list of what they bought
    total_price REAL
);

-- Initial Menu Data
INSERT INTO Menu (name, price, category) VALUES ('Beef Burger', 5.00, 'Beef');
INSERT INTO Menu (name, price, category) VALUES ('Double Beef Burger', 6.50, 'Beef');
INSERT INTO Menu (name, price, category) VALUES ('Beefy BBQ Special', 8.50, 'Beef');