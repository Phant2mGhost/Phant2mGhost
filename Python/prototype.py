#converts user input into int list
def user_input():
    binaries = []
    user_input = input("Binary Number: ")
    for b in user_input:
        b = int(b)
        binaries.append(b)
    return binaries

#checks for invalid input
def check_valid_input(binaries):
    for b in binaries:
        if b != 0 and b != 1:
            return False
            return True
            
binaries = user_input()

while not check_valid_input(binaries):
    print("Invalid input. Please enter binary number only.")
    binaries = user_input()
    
print(binaries)
