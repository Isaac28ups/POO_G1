def hievery(list1):
    for name in list1:
        print("Hi,",name)
hievery(["Isaac","Pam","Frank"])

def createlist(n):
    mylist=[]
    for i in range(n):
        mylist.append(i)
    return mylist
print(createlist(11))