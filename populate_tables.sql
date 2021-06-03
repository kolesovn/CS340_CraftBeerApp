--
-- Dumping data for table `Customers`
--

INSERT INTO `Customers` (`Customer_id`, `Customer_name`, `Customer_phone`) VALUES
(1, 'Steve', '555-new-5555'),
(2, 'Sally', '444-444-4444'),
(4, 'Optimus Prime', '111-111-borg'),
(6, 'test1', '555'),
(7, 'test2updated', '222'),
(8, 'test3', '333'),
(9, 'Gandalf', '000'),
(10, 'Pippin', '0'),
(11, 'An actual sloth', '5');

--
-- Dumping data for table `diagnostic`
--

INSERT INTO `diagnostic` (`id`, `text`) VALUES
(0, 'MySQL is working');

--
-- Dumping data for table `Orders`
--

INSERT INTO `Orders` (`Order_id`, `Customer_id`, `Order_date`) VALUES
(1, 9, '2021-05-03'),
(2, 1, '2021-05-01'),
(3, 4, '2021-05-19'),
(4, 2, '2019-05-08');

--
-- Dumping data for table `Order_products`
--

INSERT INTO `Order_products` (`Order_product_id`, `Order_id`, `Product_id`, `Quantity`) VALUES
(3, 1, 2, 2),
(4, 1, 4, 1),
(5, 2, 3, 5),
(6, 3, 1, 20);


--
-- Dumping data for table `Products`
--

INSERT INTO `Products` (`Product_id`, `Product_name`, `Supplier_id`, `Unit_cost`, `Unit_price`, `Quantity`) VALUES
(1, 'CCBC Tropicalia', 1, '8', '11', 200),
(2, 'CCBC Bibo', 1, '7', '10', 50),
(3, 'Allagash White', 2, '8', '11', 50),
(4, 'Jester King SPON', 4, '15', '20', 20),
(6, 'Allagash Moselle', 3, '10', '13', 15),
(7, 'test product', 2, '2', '3', 5);

--
-- Dumping data for table `Purchases`
--

INSERT INTO `Purchases` (`Purchase_id`, `Supplier_id`, `Purchase_date`) VALUES
(1, 2, '2021-05-04'),
(2, 1, '2021-05-01'),
(3, 4, '2021-05-11'),
(4, 1, '2021-05-12');

--
-- Dumping data for table `Purchase_products`
--

INSERT INTO `Purchase_products` (`Purchase_product_id`, `Purchase_id`, `Product_id`, `Quantity`) VALUES
(1, 1, 1, 50),
(2, 2, 3, 30),
(3, 3, 4, 10),
(4, 4, 3, 50);

--
-- Dumping data for table `Suppliers`
--

INSERT INTO `Suppliers` (`Supplier_id`, `Supplier_name`, `Supplier_phone`, `Supplier_location`) VALUES
(1, 'Creature Comforts', '555-555-5555', 'Athens, Ga'),
(2, 'Allagash', '444-444-4444', 'Portland, ME'),
(3, '3 Taverns', '333-333-3333', 'Decatur, Ga'),
(4, 'Jester King', '222-222-2222', 'Austin, Tx');



