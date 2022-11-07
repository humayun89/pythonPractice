# Determine the Price of a product  after the discount :
price=float(input("Enter the price of a product :"))
if price <=500:
    discount = 20
    discounted_price = float(price - (price * (discount / 100)))
    print(discounted_price)
elif price <=1000:
    discount = 25
    discounted_price = float(price - (price * (discount / 100)))
    print(discounted_price)
else:
    discount = 30
    discounted_price = float(price - (price * (discount / 100)))
    print(discounted_price)
# Sale of alchohol to the customer:
id_check = str(input("Show your id please : "))
age_check = float(input("age : "))
if id_check == str("yes") and age_check >= 18:
    print("Yes .You can.")
else:
    print("Sorry you cannot purchase.")

# While loop experiment:
num = 0
while num > 100:
    num = int(num+31)
    print('num', num)
# For loop small project to get the series of the numbers using range:
for x in range (50,1000,1):
     print("Number = ",x)

#  print the following pattern using for loops:1
       #  1 3
       #  1 3 5
       #  1 3 5 7
       #  1 3 5 7 9
       #  Hint : Take a look at the parameter called end  in the print function. Also, note that we need a nested loop here.

for i in range(1,10,2):
    for j in range(1, i+1 , 2):
        print(j , end = " ")
    print("")
# Again:
n = int(input("Enter the number of rows you need : "))
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()
# Once more for sequencial series in column and raw :
n = int(input("Enter the number of the rows : "))
for i in range(n):
    for j in range(i, -1, -1):
        print(j+1, end=" ")
    print()
# Same thing but different ways:
n = int(input("Enter the number of the rows : "))
for i in range(n):
    for j in range(i, -1, -1):
        print(i+1, end=" ")
    print()
# Reverse order :
n=int(input("Enter the number of raws : "))
for i in range(n):
    for j in range(i+1):
        print(n-i,end=" ")
    print()

# Again:
n=int(input("Enter the number of raws :"))
for i in range (n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(i+1,end= " ")
    print()
# Use of continue and break:
# Continue is used for skip element in condition , and go to run the next one ;where break stop in before the condition where it should be break.

# continue:
my_list = [1, 2, "stop", 3.42]
for current_element in my_list:
    if current_element == "stop":
        print("The loop will skip stop !")
        continue
    print(current_element)
# Break:
my_list=[1,2, "stop",3.42]
for current_element in my_list:
    if current_element=="stop":
        print("The loop will stop for break !")
        break
    print(current_element)

# Zip:
first_list=[1,2, "stop",4.12]
second_list=[5,7, "now", 9]
zipped_lists=zip(first_list,second_list)
print(list(zipped_lists))

