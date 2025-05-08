A = [3,4,5,6,7]
B = [5,6]
A.sort()
B.sort()

for i in range(len(A)):
    if all(x in A for x in B):
        print(True)
        break
else:
    print(False)
    

