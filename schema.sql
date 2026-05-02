CREATE TABLE menu (
    menuid INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
);

CREATE TABLE orders (
    orderid INTEGER PRIMARY KEY AUTOINCREMENT,
    menuid INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total REAL NOT NULL,
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (menuid) REFERENCES Menu(menuid)
);


--MENU ITEMS
INSERT INTO Menu (name, description, price)
VALUES 
--BEEF BURGERS
('Classic Beef', 'Juicy beef patty with lettuce & sauce', 5.00),
('Double Beef', 'Two juicy beef patties with lettuce & sauce', 6.50),
('Beefy BBQ Special', 'Smoky beef & Bacon with special sauce', 8.00),
--CHICKEN BURGERS
('Classic Chicken', 'Crispy chicken fillet with mayo', 5.50),
('Crispy Chicken Zinger', 'Crispy chicken zinger with lettuce & mayo', 7.00),
('Saucy Bacon & Chicken', 'Chicken burger w/ bacon and special sauce', 8.50),
--SIDES
('Fries', 'Crispy golden fries', 2.00),
('10 Pcs Chicken Nuggets', 'Chicken nuggets w/ Sweet & Sour Sauce', 2.50),
('Onion Rings', 'Crispy battered onion rings', 2.50),
--DRINKS
('Soft Drink', 'Refreshing carbonated beverage', 1.50),
('Milkshake', 'Creamy homemade vanilla milkshake', 3.00),
('Iced Tea', 'Chilled iced tea with lemon', 2.00);


-- Joins tables together to make it easier to read the order details with the menu item names and prices
SELECT 
    orders.orderid,
    Menu.name,
    Menu.price,
    orders.quantity,
    orders.total,
    orders.order_time
FROM orders
JOIN Menu ON orders.menuid = Menu.menuid;

ALTER TABLE Menu ADD COLUMN category TEXT;