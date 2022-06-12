-- these scripts correspond to the app Logic




-- High leavel(app) Logic
--    ----> translate 
--                     -----> Low LEVEL (DB) LOGIC

delete Product WHERE id > 1;

/*
ADMIN LOGIC
*/
--- Add Product ()

INSERT into Product 
VALUES (1 , "First Product", 100, "USD", "12345678932131",10);
INSERT into Product 
VALUES (2 , "Two Product", 200, "USD", "12378945632125",20);
INSERT into Product 
VALUES (3 , "Three Product", 300, "USD", "98765432145646",30);
INSERT into Product 
VALUES (4 , "Four Product", 400, "USD",  "45612332981987",40);



/*
CLIENT LOGIC
*/
BEGIN;
-- Sing UPDATE
INSERT into CLIENT 
VALUES (1 , "First Client", "firs_client@t.com", "+1234567896",  true);

-- add to bag
INSERT into bag 
VALUES (2 , 1);

INSERT into bagItems 
VALUES (1 , 2, 10);

UPDATE Product
Set quantity = quantity - 10 
where id = 2;
COMMIT;

-- view bagItems

Select * from bagItems
where bag_id = 1;


/*
API Logic

*/

UPDATE Product
Set name = "Second Product" 
where name = "Secont Product";