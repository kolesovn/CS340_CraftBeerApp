--
-- Table structure for table `Customers`
--
DROP TABLE IF EXISTS `Customers`;
CREATE TABLE `Customers` (
  `Customer_id` int(11) NOT NULL,
  `Customer_name` varchar(50) NOT NULL,
  `Customer_phone` varchar(50) NOT NULL
)ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Orders`
--
DROP TABLE IF EXISTS `Orders`;
CREATE TABLE `Orders` (
  `Order_id` int(11) NOT NULL,
  `Customer_id` int(11) NOT NULL,
  `Order_date` date NOT NULL
);
-- ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `Order_products`
--
DROP TABLE IF EXISTS `Order_products`;
CREATE TABLE `Order_products` (
  `Order_product_id` int(11) NOT NULL,
  `Order_id` int(11) NOT NULL,
  `Product_id` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL
);
-- ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `Products`
--
DROP TABLE IF EXISTS `Products`;
CREATE TABLE `Products` (
  `Product_id` int(11) NOT NULL,
  `Product_name` varchar(50) NOT NULL,
  `Supplier_id` int(11) NOT NULL,
  `Unit_cost` decimal(10,0) NOT NULL,
  `Unit_price` decimal(10,0) NOT NULL,
  `Quantity` int(11) DEFAULT NULL 
);
-- ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `Purchases`
--
DROP TABLE IF EXISTS `Purchases`;
CREATE TABLE `Purchases` (
  `Purchase_id` int(11) NOT NULL,
  `Supplier_id` int(11) NOT NULL,
  `Purchase_date` date NOT NULL
);
-- ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `Purchase_products`
--
DROP TABLE IF EXISTS `Purchase_products`;
CREATE TABLE `Purchase_products` (
  `Purchase_product_id` int(11) NOT NULL,
  `Purchase_id` int(11) NOT NULL,
  `Product_id` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL
);
-- ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- --------------------------------------------------------

--
-- Table structure for table `Suppliers`
--
DROP TABLE IF EXISTS `Suppliers`;
CREATE TABLE `Suppliers` (
  `Supplier_id` int(11) NOT NULL,
  `Supplier_name` varchar(50) NOT NULL,
  `Supplier_phone` varchar(50) NOT NULL,
  `Supplier_location` varchar(250) NOT NULL
); 
-- ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Indexes for table `Customers`
--
ALTER TABLE `Customers`
  ADD PRIMARY KEY (`Customer_id`);


--
-- Indexes for table `Orders`
--
ALTER TABLE `Orders`
  ADD PRIMARY KEY (`Order_id`),
  ADD KEY `Customer_id` (`Customer_id`);

--
-- Indexes for table `Order_products`
--
ALTER TABLE `Order_products`
  ADD PRIMARY KEY (`Order_product_id`),
  ADD KEY `Order_id` (`Order_id`),
  ADD KEY `Product_id` (`Product_id`);

--
-- Indexes for table `Products`
--
ALTER TABLE `Products`
  ADD PRIMARY KEY (`Product_id`),
  ADD KEY `Supplier_id` (`Supplier_id`);

--
-- Indexes for table `Purchases`
--
ALTER TABLE `Purchases`
  ADD PRIMARY KEY (`Purchase_id`),
  ADD KEY `Supplier_id` (`Supplier_id`);

--
-- Indexes for table `Purchase_products`
--
ALTER TABLE `Purchase_products`
  ADD PRIMARY KEY (`Purchase_product_id`),
  ADD KEY `Purchase_id` (`Purchase_id`),
  ADD KEY `Product_id` (`Product_id`);


--
-- Indexes for table `Suppliers`
--
ALTER TABLE `Suppliers`
  ADD PRIMARY KEY (`Supplier_id`);


--
-- AUTO_INCREMENT for table `Customers`
--
ALTER TABLE `Customers`
  MODIFY `Customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `Orders`
--
ALTER TABLE `Orders`
  MODIFY `Order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Order_products`
--
ALTER TABLE `Order_products`
  MODIFY `Order_product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `Products`
--
ALTER TABLE `Products`
  MODIFY `Product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `Purchases`
--
ALTER TABLE `Purchases`
  MODIFY `Purchase_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Purchase_products`
--
ALTER TABLE `Purchase_products`
  MODIFY `Purchase_product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `sample`
--
ALTER TABLE `sample`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Suppliers`
--
ALTER TABLE `Suppliers`
  MODIFY `Supplier_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;


--
-- Constraints for table `Orders`
--
ALTER TABLE `Orders`
  ADD CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`Customer_id`) REFERENCES `Customers` (`Customer_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Order_products`
--
ALTER TABLE `Order_products`
  ADD CONSTRAINT `Order_products_ibfk_1` FOREIGN KEY (`Order_id`) REFERENCES `Orders` (`Order_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Order_products_ibfk_2` FOREIGN KEY (`Product_id`) REFERENCES `Products` (`Product_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Products`
--
ALTER TABLE `Products`
  ADD CONSTRAINT `Products_ibfk_1` FOREIGN KEY (`Supplier_id`) REFERENCES `Suppliers` (`Supplier_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Purchases`
--
ALTER TABLE `Purchases`
  ADD CONSTRAINT `Purchases_ibfk_1` FOREIGN KEY (`Supplier_id`) REFERENCES `Suppliers` (`Supplier_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Purchase_products`
--
ALTER TABLE `Purchase_products`
  ADD CONSTRAINT `Purchase_products_ibfk_1` FOREIGN KEY (`Purchase_id`) REFERENCES `Purchases` (`Purchase_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Purchase_products_ibfk_2` FOREIGN KEY (`Product_id`) REFERENCES `Products` (`Product_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

--
-- Sample data for table `Customers`
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
-- Sample data for table `Orders`
--

INSERT INTO `Orders` (`Order_id`, `Customer_id`, `Order_date`) VALUES
(1, 9, '2021-05-03'),
(2, 1, '2021-05-01'),
(3, 4, '2021-05-19'),
(4, 2, '2019-05-08');

--
-- Sample data for table `Order_products`
--

INSERT INTO `Order_products` (`Order_product_id`, `Order_id`, `Product_id`, `Quantity`) VALUES
(3, 1, 2, 2),
(4, 1, 4, 1),
(5, 2, 3, 5),
(6, 3, 1, 20);


--
-- Sample data for table `Products`
--

INSERT INTO `Products` (`Product_id`, `Product_name`, `Supplier_id`, `Unit_cost`, `Unit_price`, `Quantity`) VALUES
(1, 'CCBC Tropicalia', 1, '8', '11', 200),
(2, 'CCBC Bibo', 1, '7', '10', 50),
(3, 'Allagash White', 2, '8', '11', 50),
(4, 'Jester King SPON', 4, '15', '20', 20),
(6, 'Allagash Moselle', 3, '10', '13', 15),
(7, 'test product', 2, '2', '3', 5);

--
-- Sample data for table `Purchases`
--

INSERT INTO `Purchases` (`Purchase_id`, `Supplier_id`, `Purchase_date`) VALUES
(1, 2, '2021-05-04'),
(2, 1, '2021-05-01'),
(3, 4, '2021-05-11'),
(4, 1, '2021-05-12');

--
-- Sample data for table `Purchase_products`
--

INSERT INTO `Purchase_products` (`Purchase_product_id`, `Purchase_id`, `Product_id`, `Quantity`) VALUES
(1, 1, 1, 50),
(2, 2, 3, 30),
(3, 3, 4, 10),
(4, 4, 3, 50);

--
-- Sample data for table `Suppliers`
--

INSERT INTO `Suppliers` (`Supplier_id`, `Supplier_name`, `Supplier_phone`, `Supplier_location`) VALUES
(1, 'Creature Comforts', '555-555-5555', 'Athens, Ga'),
(2, 'Allagash', '444-444-4444', 'Portland, ME'),
(3, '3 Taverns', '333-333-3333', 'Decatur, Ga'),
(4, 'Jester King', '222-222-2222', 'Austin, Tx');