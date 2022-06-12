from pydoc import describe
from numpy import append
from Select_db import *
from Inser_db import *
from Delet_db import *
from os import *
option = 0
cls = "cls"
while option != 4:
    print("What operation do you want to do?")
    print("1. Add Product")
    print("2. Delete Product")
    print("3. View Table")
    print("4. Exit")
    option = input(">>> ")
    if int(option) == 1:
        addprod()
        system(cls)
    elif int(option) == 2:
        DelProd(6)
        system(cls)
    elif int(option) == 3:
        showtable()
        TableName = input("Enter what a table you want to see >>  ")
        system(cls)
        execute(TableName)
    else :
        option = 4   