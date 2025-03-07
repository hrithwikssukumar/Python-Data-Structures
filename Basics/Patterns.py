
#"1"

for i in range(1,8):
    for j in range(1,6):
        if j == 4-i or j == 3 or i ==7:
            print("*",end="")
        else:
            print(" ",end="")
    print() 


 #"4"

 for i in range(1,8):
    for j in range(1,8):
        if j == 5 or i == 5 or j == 6-i:
            print("*",end="")
        else:
            print(" ",end="")
    print() 



#"3"

for i in range(1,8):
    for j in range(1,6):
        if i == 1 or i == 4 or i == 7 or j ==5:
            print("*",end="")
        else:
            print(" ",end="")
    print()        



#"I"


for i in range(1,8):
    for j in range(1,8):
        if i == 1 or j == 4 or i == 7 :
            print("*",end="")
        else:
            print(" ",end="")
    print()