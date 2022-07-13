word = 'Help' + 'A'
print(word)

print(word[4])
print(word[0:2])
print(word[2:4])

c = "moratuwa university"
word = c[-4]+c[-2]
word += c[1:3]+c[0]
print (word)

c = "pythontutor"
word = c[1] + c[-2] + c[-4]
word += c[-3:-1] + c[0]
print (word)

str1 = "xyz"
str2 = 'pqr'
a = str2
print ((id(a) == id(str2)))

x = "Computer Science and Engineering"
print (x[:3]+x[6]+x[9:12]+x[-11:-8])

for i in range(3,2,-1): 
   print('!'*i)
