# assignment1 on list of objects with 
class ProdDetails:
    def __init__(self, pId, pname, price, manuName):
        self.pId=pId
        self.pname = pname
        self.price = price
        self.manuName = manuName
        print("This is ProdDetails constructor")

    def __repr__(self):
        return self.pId+"\t"+self.pname+"\t"+str(self.price)+"\t"+self.manuName

    def __hash__(self):
        return hash((self.pId, self.pname, self.price, self.manuName))

    def __eq__(self, obj):
        return isinstance(obj, ProdDetails) and obj.pId == self.pId

    def __ne__(self, obj):
        return not self == obj

    def met(self):
        print("This is met in ProdDetails class: "+self.pId+"\t"+self.pname+"\t"+str(self.price)+"\t"+self.manuName)


products = [ProdDetails("P10","aaa",50,"x1"), ProdDetails("P20","bbb",85,"x2"), ProdDetails("P30","ccc",60,"x3")]


#sorted list of products in ascending order
print("List of products in ascending price order")
products.sort(key=lambda x: x.price)
for val in products:
    print(val)
print("List of products in descending price order")
products.sort(key=lambda x: x.price,  reverse=True)
for val in products:
    print(val)

#List stores the duplicates and maintains insertion order
products.append(ProdDetails("P40","ddd", 94,"x1"))
products.append(ProdDetails("P10","aaa", 50,"x1"))

print("List of objects in products")
for val in products:
    print(val)
#extending a list with a anather compatible list
new_products = [ProdDetails("P60","eee",58,"x3"), ProdDetails("P70","abc",80,"x5")]
print("List of objects in new_products")
for val in new_products:
    print(val)
products.extend(new_products)
print("List of objects in products after extension")
for val in products:
    print(val)
#adding incompatible / wrong objects
incompatible_list=[56,34]
products1=products
products1.extend(incompatible_list)
print("List of objects in products1")
for val in products1:
    print(val)
#slicing to remove the newly added incompatible objects
products2 = products1[:-(len(incompatible_list))]
print("List of objects in products2")
for val in products2:
    print(val)
#slicing for selecting a subset of objects
temp = products2[-3:]
print("List of the last three objects")
for val in temp:
    print(val)
temp = products2[1:5]
print("List of selected objects")
for val in temp:
    print(val)
# converting into set of products to get unique objects
set_products=set(products2)
print("set of unique objects")
for val in set_products:
    print(val)

