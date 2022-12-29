'''
* Develop a calculator of integers 
* The program has to ask for two numbers and do the basic operations
* Controle the exceptions that can produce
'''
try:
    number1 = int(input("Introduce the first number: "))
    number2 = int(input("Introduce the second number: "))
except: 
    print("You didn't introduce a number. Default values will be set")
    number1 = 1
    number2 = 1
    
addition = number1 + number2    
subtraction = number1 - number2
multiplication = number1 * number2
try:
    division = round(number1/number2,2)
except:
    print("ERROR in the division")
    division = "ERROR"

print("The results are: ")
print(f"The result of the additiion is : {addition}")
print(f"The result of the subtraction is : {subtraction}")
print(f"The result of the multiplication is : {multiplication}")
print(f"The result of the division is : {division}")