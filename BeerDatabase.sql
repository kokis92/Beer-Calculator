
--- Create beer table with values 
Create Table Beer(
BeerID int IDENTITY (1,1) NOT NULL,
BeerName VARCHAR(255),
Calories int, 
ABV DECIMAL(5,2),
BeerType VARCHAR(255)
)

--- Needed to add a primary key to the Beer Table 
ALTER TABLE Beer
ADD PRIMARY KEY (BeerID);

--- Selects all the values in the Beer Table 
Select * from Beer

--- Create the BeerStore Table with primary keys and Foreign keys 
Create Table BeerStore(
StoreID int IDENTITY (1,1) NOT NULL,
StoreName VARCHAR(255),
BeerPrice DECIMAL(5,2), 
PackSize int,
BeerID int,
PRIMARY KEY (StoreID),
FOREIGN KEY (BeerID) REFERENCES Beer(BeerID)
)

-- Retrieves all the values from the two tables 
select * from BeerStore
SElECT * From Beer

--- Adds values to the Beer Table 
INSERT INTO Beer(BeerName, Calories, ABV, BeerType)
VALUES('Pacifico Clara',145, 4.4, 'Pale Lager')

--- Adds values to the BeerSto Table 
INSERT INTO BeerStore(StoreName, BeerPrice, PackSize, BeerID)
VALUES('Safeway',16.99, 12, 2)


--- SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
--- FROM Orders
--- INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;

--- Retrieves all the beers where ABV is equal to 4.4 
Select BeerName, BeerType 
from Beer
WHERE ABV = 4.4

--- Retrieves prices for pacifico 12 pack
Select b.BeerName, b.Calories, b.ABV, b.BeerType, s.BeerPrice, s.StoreName
From Beer b 
INNER JOIN BeerStore s ON b.BeerID =s.BeerID
WHere BeerName = 'Pacifico Clara' and PackSize = 12


