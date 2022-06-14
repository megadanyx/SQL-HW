## ORM (object relation mapping)

from numpy import save
from orm.Product import Product

# p1 = Product(5, "My Prod", 100, "UDS", "1100464008403", 10)
# p2 = Product(2, "Second", 100,"UDS","213564688453",10)
# p1.create()
# p1.name = "Modify"
# p1.save()
# print(p2)
# products = Product.all()
# print(*products, sep = "\n")
prod = Product.get(0)
print(prod)