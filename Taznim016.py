#task1
name = "Taznim Juwana Orin"
age = 20
print ("my name is " + name+ "and i am " + str(age)+ "years old.")

#task2
num1 = 12
num2 = 8.2
num_float = float(num1)
num_int = int(num2)
print ("integer number is" +str(num1)+"num1 to a float="+ str(num_float)+"float number is" +str(num2)+"num2 to int="+str(num_int))

#task3
sentence = "Python programming is fun!"
print("length of "+sentence+"is"+str(len(sentence)))
print("8th character is" +str(sentence[8]))
substring = sentence [0:6]
print(substring)
print("i enjoy it" +substring)

#task4
fruit=["apple", "banana", "cherry","date"]
fruit.append("grape")
fruit.remove("remove")
print(len(fruit))
sliced_fruits = frui[2:4]
print (sliced_fruits)
extrafruit=["kiwi","lemon"]
combinedfruit = sliced_fruits+extrafruit
print(combinedfruit)

#task5
num = 1
if num % 2==0:
    print("even")
else:
    print("odd")

#task6 
for num in range(1,11):
    print(num)
for num in range(1,101):
    sum=0
    sum=sum+num
    print(sum)

#task7
num = 7  
num1 =  num * num;
print("\n")
print(num1)
print("\n")
def is_prime(num):
     flag= False
     for n in range(2,num):
      if num % n ==0:
       flag = True
       break;
     return flag
print(is_prime(1))
print(is_prime(29))

#task8
student ={"Name":"John","Age":"23","Grade":"A"} 
course ={"Name":"Bangla"} 
print("\n")
print(student)
print(course)
x=student["Name"]
print(x)
for x in student:
   print(x)



      
    
    