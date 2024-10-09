# Queries

## Question 1

* Prompt: What is the most popular dish?
* Query: 
```mysql
SELECT d.Name, SUM(o.Quantity) AS TotalOrdered
FROM `Order` o
JOIN `Dish` d ON o.DishId = d.Id
GROUP BY d.Id
ORDER BY TotalOrdered DESC
LIMIT 1;
```

* DB Response: 
```text
[[(Spaghetti Bolognese, 2,)]]
```

* Friendly Response: Spaghetti Bolognese

## Question 2

* Prompt: What Customer has the most orders?
* Query: 
```mysql
SELECT c.Name, COUNT(o.Id) AS OrderCount
FROM `Order` o
JOIN `Customer` c ON o.CustomerId = c.Id
GROUP BY c.Id
ORDER BY OrderCount DESC
LIMIT 1;
```

* DB Response: 
```text
[[(John Smith, 2)]]
```

* Friendly Response: John Smith

## Question 3

* Prompt: What is the most recent order?
* Query: 
```mysql
SELECT o.Id, c.Name, d.Name AS DishName, o.OrderDate
FROM `Order` o
JOIN `Customer` c ON o.CustomerId = c.Id
JOIN `Dish` d ON o.DishId = d.Id
ORDER BY o.OrderDate DESC
LIMIT 1;
```

* DB Response: 
```text
[[(5, Tyler, Burns, Margherita Pizza, 2024-10-04 12:32:00)]]
```

* Friendly Response: Margherita Pizza

## Question 4

* Prompt: What is the least ordered dih?
* Query: 
```mysql
SELECT d.Name, SUM(o.Quantity) AS TotalOrdered
FROM `Order` o
JOIN `Dish` d ON o.DishId = d.Id
GROUP BY d.Id
ORDER BY TotalOrdered ASC
LIMIT 1;
```

* DB Response: 
```text
[[(Quesadilla, 1)]]
```

* Friendly Response: Quesadilla

## Question 5

* Prompt: What is the average dish price?
* Query: 
```mysql
SELECT AVG(Price) AS AveragePrice
FROM `Dish`;
```

* DB Response: 
```text
[[(10.99,)]]
```

* Friendly Response: 10.99

## Question 6

* Prompt: What customer spent the most money?
* Query: 
```mysql
SELECT c.Name, SUM(d.Price * o.Quantity) AS TotalSpent
FROM `Order` o
JOIN `Customer` c ON o.CustomerId = c.Id
JOIN `Dish` d ON o.DishId = d.Id
GROUP BY c.Id
ORDER BY TotalSpent DESC
LIMIT 1;
```

* DB Response: 
```text
[[(John Smith, 36.97)]]
```

* Friendly Response: John Smith

## Question 7

* Prompt: What is the most expensive dish
* Query: 
```mysql
SELECT Name, Price
FROM `Dish`
ORDER BY Price DESC
LIMIT 1;
```

* DB Response: 
```text
[[(spaghetti Bolognese, 12.99)]]
```

* Friendly Response: Spaghetti Bolognese
