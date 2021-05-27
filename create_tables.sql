--
-- Table structure for table `Customers`
--

CREATE TABLE `Customers` (
  `Customer_id` int(11) NOT NULL,
  `Customer_name` varchar(50) NOT NULL,
  `Customer_phone` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `diagnostic`
--

CREATE TABLE `diagnostic` (
  `id` int(11) NOT NULL,
  `text` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- --------------------------------------------------------

--
-- Table structure for table `Orders`
--

CREATE TABLE `Orders` (
  `Order_id` int(11) NOT NULL,
  `Customer_id` int(11) NOT NULL,
  `Order_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `Order_products`
--

CREATE TABLE `Order_products` (
  `Order_product_id` int(11) NOT NULL,
  `Order_id` int(11) NOT NULL,
  `Product_id` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `Products`
--

CREATE TABLE `Products` (
  `Product_id` int(11) NOT NULL,
  `Product_name` varchar(50) NOT NULL,
  `Supplier_id` int(11) NOT NULL,
  `Unit_cost` decimal(10,0) NOT NULL,
  `Unit_price` decimal(10,0) NOT NULL,
  `Quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `Purchases`
--

CREATE TABLE `Purchases` (
  `Purchase_id` int(11) NOT NULL,
  `Supplier_id` int(11) NOT NULL,
  `Purchase_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `Purchase_products`
--

CREATE TABLE `Purchase_products` (
  `Purchase_product_id` int(11) NOT NULL,
  `Purchase_id` int(11) NOT NULL,
  `Product_id` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `sample`
--

CREATE TABLE `sample` (
  `ID` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Quantity` int(11) NOT NULL,
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Suppliers`
--

CREATE TABLE `Suppliers` (
  `Supplier_id` int(11) NOT NULL,
  `Supplier_name` varchar(50) NOT NULL,
  `Supplier_phone` varchar(50) NOT NULL,
  `Supplier_location` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Indexes for table `Customers`
--
ALTER TABLE `Customers`
  ADD PRIMARY KEY (`Customer_id`);

--
-- Indexes for table `diagnostic`
--
ALTER TABLE `diagnostic`
  ADD PRIMARY KEY (`id`);

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
-- Indexes for table `sample`
--
ALTER TABLE `sample`
  ADD PRIMARY KEY (`ID`);

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
  ADD CONSTRAINT `Order_products_ibfk_1` FOREIGN KEY (`Order_id`) REFERENCES `Orders` (`Order_id`),
  ADD CONSTRAINT `Order_products_ibfk_2` FOREIGN KEY (`Product_id`) REFERENCES `Products` (`Product_id`);

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

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
