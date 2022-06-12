from connection import *
def showtable():  
    mycursor = mydb.cursor()
    sql = "Show tables"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("Exist Tables : ")
    for x in myresult: 
        name = x[0]
        print(">>" , name.capitalize())
    return myresult

def execute(table): 
    mycursor = mydb.cursor()
    sql = "SELECT * FROM %s"% table
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print()
    for x in myresult:
        print(x)
    print()
    return myresult
