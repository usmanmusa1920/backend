# E-commerce System Database

We are building an e-commerce system, and we need to manage products, orders, and customers.

## Database Schema:

Start by designing the schema with tables like:

- Customers: Stores customer data.
- Products: Stores product details.
- Orders: Links customers to their purchases.
- Order_Items: Stores which products are in each order.

```sh
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    stock INT
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Order_Items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
```

## Queries:

Here are a few example queries for this system.

Insert a new customer:

```sh
INSERT INTO Customers (first_name, last_name, email) VALUES ('Abdulhakeem', 'Sanusi', 'abdulhakeemsanusi@gmail.com');
```

View all products:

```sh
SELECT * FROM Products;
```

Create a new order (including multiple products):

```sh
INSERT INTO Orders (customer_id) VALUES (1);
# Assuming customer_id 1 is Abdulhakeem Sanusi

# Get the last inserted order ID (assuming it's auto-incremented)
SET @order_id = LAST_INSERT_ID();

INSERT INTO Order_Items (order_id, product_id, quantity, price) VALUES (@order_id, 1, 3, 19.99);
# Adds 3 units of product_id 2 to the order
```

View orders for a specific customer:

```sh
SELECT o.order_id, o.order_date, oi.product_id, oi.quantity, oi.price
FROM Orders o
JOIN Order_Items oi ON o.order_id = oi.order_id
WHERE o.customer_id = 1;
# Orders for customer with ID 1
```

Update product stock:

```sh
UPDATE Products
SET stock = stock - 3
WHERE product_id = 2;
# Reduces stock by 3 units for product_id 2
```

## Specific Problem Example:

If you're facing a problem, like retrieving products that a customer has ordered in the last month, you might need a query like this:

```sh
SELECT p.name, SUM(oi.quantity) AS quantity_ordered
FROM Products p
JOIN Order_Items oi ON p.product_id = oi.product_id
JOIN Orders o ON oi.order_id = o.order_id
WHERE o.customer_id = 1
AND o.order_date > NOW() - INTERVAL 1 MONTH
GROUP BY p.product_id;
```

## Troubleshooting:

If you’re facing issues like performance problems with large datasets, or if certain queries are slow, I can also help you optimize your queries by using indexes or adjusting the schema design.
