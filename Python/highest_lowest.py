numbers = [12, 43, 54, 67, 35, 20, 5, 9]
print(f"Numbers: {numbers}")                      
#Highest
number = numbers[0]
for n in numbers:
  if (n>number):
      number = n
print(f"Highest: {number}")

#Lowest
number = numbers[0]
for n in numbers:
    if (n<number):
        number = n
print(f"Lowest: {number}")