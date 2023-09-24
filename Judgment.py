hungry=True


if hungry:
   print("eating!!!")
rainy=True


if rainy:
   print("drive the car") 
else:
   print("walk")

score=70
if score==100:
   print("i will give u 1000 dollar") 
elif score>=80:
   print("i will give u 500 dollar")
elif score>=60:
   print("i will give u 100 dollar") 
else:
   print("u need to give me 300 dollar")      



score=100
rainy=False
if score==100 and rainy:
   print("i will give u 1000 doiiar")
else: 
    print("u give me 100 dollar")

scorse=100
rainy=True
if score==100 or rainy:
   print ("i will give u 1000 dollar")
else:
   print("u give me 100 dollar")


scorse=100
rainy=True
if score==100 or not (rainy):
   print ("i will give u 1000 dollar")
else:
   print("u give me 100 dollar")
   print(1)


def max_num(num1,num2,num3):
   if num1>=num2 and num1>=num3:
      return num1
   elif num2>=num1 and num2>=num3:
      return num2
   else:
      return num3
print(max_num(10,3,5))






































































