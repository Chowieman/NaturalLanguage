DROP TABLE IF EXISTS `Order`;
DROP TABLE IF EXISTS `Dish`;
DROP TABLE IF EXISTS `Customer`;

CREATE TABLE `Customer` (
    `Id` INT,
    `Name` VARCHAR(100) NOT NULL,
    `Email` VARCHAR(100) NOT NULL,
    `Phone` VARCHAR(20) NULL,
    PRIMARY KEY (`Id`)
);

CREATE TABLE `Dish` (
    `Id` INT,
    `Name` VARCHAR(100) NOT NULL,
    `Price` DECIMAL(10, 2) NOT NULL,
    `Description` VARCHAR(200) NULL,
    PRIMARY KEY (`Id`)
);

CREATE TABLE `Order` (
    `Id` INT,
    `CustomerId` INT NOT NULL,
    `DishId` INT NOT NULL,
    `Quantity` INT NOT NULL,
    `OrderDate` DATETIME NOT NULL,
    FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`Id`),
    FOREIGN KEY (`DishId`) REFERENCES `Dish` (`Id`)
);
