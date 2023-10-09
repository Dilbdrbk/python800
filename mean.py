l1=[2,3,5,6]
total=0
index=0
mean=0

while index <len(l1):
    item = l1[index]
    total+=item
    mean=total/len(l1)
    index=index+1
print("Mean:",mean)