INSERT INTO `Customer` (`Id`, `Name`, `Email`, `Phone`) VALUES
    (1, 'John Smith', 'john@example.com', '555-1234'),
    (2, 'Alice Brown', 'alice@example.com', '555-5678');
    (3, 'Tyler Burns', 'tyler@example.com', '555-9012');
    (4, 'Skyler Magula', 'skyler@example.com', '555-3456');

INSERT INTO `Dish` (`Id`, `Name`, `Price`, `Description`) VALUES
    (1, 'Spaghetti Bolognese', 12.99, 'Classic Italian pasta with meat sauce'),
    (2, 'Margherita Pizza', 9.99, 'Fresh tomato, mozzarella, and basil');
    (3, 'Quesadilla', 10.99, 'Seasoned chicken and mexican blend cheese');
    (4, 'Onion Rings', 7.99, 'Fresh Onion fried');

INSERT INTO `Order` (`Id`, `CustomerId`, `DishId`, `Quantity`, `OrderDate`) VALUES
    (1, 1, 1, 2, '2024-10-01 19:30:00'),
    (2, 2, 2, 1, '2024-10-02 18:45:00');
    (3, 1, 3, 1, '2024-10-02 08:01:00');
    (4, 2, 4, 2, '2024-10-03 10:56:00');
    (5, 3, 2, 1, '2024-10-04 12:32:00');
