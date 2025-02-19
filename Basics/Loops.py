
#Loop for finding the sum of a number values

number = int(input("Enter a number"))
sum=0
for i in str(number):
    sum+=int(i)
print(sum) 


def sum_of_digits(number):
    total=0
    for i in str(number):
        total += int(i)
        return total
num= int(input("Enter a number"))
result= sum_of_digits(num)
print(f"The total sum is :{result}")






a = [7,3,8,1,4]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]< a[j]:
            a[i],a[j]=a[j],a[i]
print(a)  