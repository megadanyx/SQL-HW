from connection import *
def addprod():   
    MyProd = []
    describ_Prod = ["id", "name" , "price", "value", "bar code ", "quantity" ]
    for x in range(6):
        index = describ_Prod[x]
        x = input(f"{index:<8} >> " )
        MyProd.append(x)
    mycursor = mydb.cursor()
    sql = "INSERT Into Product VALUES(%s ,%s, %s, %s , %s ,%s)" 
    mycursor.execute(sql,MyProd)
    mycursor.execute("Commit;")