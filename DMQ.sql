-- Select Queries
SELECT * FROM `Customers`;
SELECT * FROM `Products`;
SELECT * FROM `Suppliers`;
SELECT * FROM `Orders`;
SELECT * FROM `Order_products`;
SELECT * FROM `Purchases`;
SELECT * FROM `Purchase_products`;
-- Select Queries for Search/FK Dropdowns
SELECT Supplier_id, Supplier_name FROM Suppliers;
SELECT * FROM Products WHERE Product_name LIKE %s;
SELECT Customer_id, Customer_name FROM Customers;
SELECT Product_id, Product_name FROM Products;
SELECT Order_id FROM Orders;
SELECT Purchase_id, Supplier_id FROM Purchases;

-- Search Queries
SELECT * FROM `Customers` WHERE `Customer_name` = :search_query;
SELECT * FROM `Products` WHERE `Product_name` = :search_query;
SELECT * FROM `Suppliers` WHERE `Supplier_name` = :search_query;
SELECT * FROM `Orders` WHERE `Order_id` = :search_query;
SELECT * FROM `Order_products` WHERE `Order_product_id` = :search_query;
SELECT * FROM `Purchases` WHERE `Purchase_id` = :search_query;
SELECT * FROM `Purchase_products` WHERE `Purcahse_products_id` = :search_query;

-- Insert Queries
INSERT INTO `Customers` (`Customer_name`, `Customer_phone`) VALUES (name, phone);
INSERT INTO `Orders` (`Customer_id`, `Order_date`) VALUES (cus_id, ord_date);
INSERT INTO `Order_products` (`Order_id`, `Product_id`, `Quantity`) VALUES (order_id, product_id, quan);
INSERT INTO `Products` (`Product_name`, `Supplier_id`, `Unit_cost`, `Unit_price`, `Quantity`) VALUES (name, supplier_id, cost, price, quan);
INSERT INTO `Purchases` (`Supplier_id`, `Purchase_date`) VALUES (supplier_id, pur_date);
INSERT INTO `Purchase_products` (`Purchase_id`, `Product_id`, `Quantity`) VALUES (pur_id, prod_id, quan);
INSERT INTO `Suppliers` (`Supplier_name`, `Supplier_phone`, `Supplier_location`) VALUES (name, phone, location);

-- Delete Query
DELETE FROM Products WHERE Product_id = %s

-- Update Query
UPDATE `Customers` SET `Customer_name` = :cus_name, `Customer_phone` = :cus_phone WHERE `Customer_id` = :cidinput;