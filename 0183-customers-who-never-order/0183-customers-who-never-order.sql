# Write your MySQL query statement below
#Join Method
SELECT name as Customers
FROM Customers LEFT JOIN Orders ON Customers.id=Orders.customerId
WHERE customerId is null


# SELECT name AS Customers
# FROM Customers
# WHERE id NOT IN(SELECT customerID FROM Orders)