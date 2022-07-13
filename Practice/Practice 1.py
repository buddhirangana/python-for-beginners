mark = 55
if mark <= 39: grade = 'D'
elif mark < 55 : grade = 'C'
elif mark < 70 : grade = 'B'
else: grade = 'A'
print (grade)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[2][2] = 10
print(matrix)

a=0
for i in range(2,4):
    a=a+i
print(a)

num1=2
while (num1>0):
    num2=2
    while (num2>0):
        print("Sri Lanka")
        num2=num2-1
    num1=num1-1

tot=0
for num in range(5):
    if num==3:
        break
    tot=tot+num
print(tot)

numbers = [3,2,5,7,8]
count = 0
for number in numbers:
    count+=1
    if number==1:
        break
else:
    count=-1
print(count)

numbers = [3,2,5,7,8]
count = 0
for number in numbers:
    count+=1
    if number==5:
        break
else:
    count=-1
print(count)
