#for loop euta condition me rukhxa vaney while loop lai infinite time run garna milxa
#while
#syntax while true:
#while condition:

l1 = [2,3,5,6]
total = 0
index = 0

while index <len(l1):
    item = l1[index]
    total += item
    index = index + 1

print("total = ", total)

