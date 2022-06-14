from numpy import equal, prod
from .Connector import *
# Modelul tabelului SQL Product

class Product:
    def __init__(self, id, name, price_value, price_unit, bar_code, quantity ):
        self.id = id
        self.name = name
        self.price_value = price_value
        self.price_unit = price_unit
        self.bar_code = bar_code
        self.quantity = quantity
    
    def create(self):
        mycursor = mydb.cursor()
        mycursor.execute(f"INSERT INTO product (id, name, price_value, price_unit, bar_code, quantity)\
            VALUES ({self.id},  \"{self.name}\",  {self.price_value},  \"{self.price_unit}\",  \"{self.bar_code}\",  {self.quantity});")
        mydb.commit()
        mycursor.close()
        mydb.close()
    def save(self):
        mycursor = mydb.cursor()
        sql = f"UPDATE product SET name=\"{self.name}\" , price_value={self.price_value}, price_unit=\"{self.price_unit}\", bar_code=\"{self.bar_code}\", quantity={self.quantity} WHERE id = {self.id};"
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()

        # HW1 Finis Delete Method
    def delet(id):
        mycursor = mydb.cursor()
        mycursor.execute(f"DELETE FROM product WHERE id = {id};")
        mydb.commit()
        mycursor.close()
        mydb.close()
    
    def get(id):
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM product WHERE id = {id};")
        # HW 2 : Write a condition that returns None when there is no product anvalible
        product = mycursor.fetchall().copy()
        if len(product) == 1 :
           return product[0]
        else : 
           return None 
        
    def all():
        mycursor = mydb.cursor()
        mycursor.execute(f"Select * from product;")
        products = mycursor.fetchall()
        return products

    def __str__(self):
        return f"Product id {self.id}"
