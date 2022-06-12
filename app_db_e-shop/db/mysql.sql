-------------------------------------------------------
create TABLE Product (
    id integer not null auto_increment PRIMARY key ,
    name varchar(121),
    price_value numeric,
    price_unit varchar(5),
    bar_code varchar(15) UNIQUE,
    quantity integer
)
-------------------------------------------------------

-------------------------------------------------------
create TABLE Client (
    id integer not null auto_increment PRIMARY key,
    name varchar(30),
    Email varchar(121) UNIQUE,
    Phone varchar(21)  UNIQUE,
    is_vip boolean DEFAULT false
);
-------------------------------------------------------

-------------------------------------------------------
CREATE TABLE Bag(
    id integer primary key,
    Client_id integer not null,
    CONSTRAINT sk_bag FOREIGN KEY(client_id) 
    REFERENCES Client(id)

);

alter Table Bag add CONSTRAINT sk_bag FOREIGN KEY(client_id) 
REFERENCES Client(id);
-------------------------------------------------------


-------------------------------------------------------
CREATE TABLE bagItems(
    bag_id integer not null,
    product_id integer not null,
    quantity integer default 1 
);
alter Table bagItems 
add CONSTRAINT fk_bagItem FOREIGN KEY(bag_id) 
REFERENCES Bag(id);

alter Table bagItems 
add CONSTRAINT fk_Prod FOREIGN KEY(product_id) 
REFERENCES Product(id);
-------------------------------------------------------


-------------------------------------------------------
 INSERT INTO Client(name, is_vip )values ("Mihai Rotari" , true);
-------------------------------------------------------


-------------------------------------------------------
 SELECT * from Client where count(name) > 11;
-------------------------------------------------------

-------------------------------------------------------
 DELETE from Client where id = 2;
-------------------------------------------------------

-------------------------------------------------------
select * from Client where is_vip=0;
-------------------------------------------------------

-------------------------------------------------------
ALTER TABLE Client
ADD Email varchar(255);
-------------------------------------------------------

-------------------------------------------------------
UPDATE Client
SET Email='Leo@gmal.com'
WHERE id=5;
-------------------------------------------------------

-------------------------------------------------------
drop TABLE Product;
-------------------------------------------------------