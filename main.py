# Python lection 1 homework
# homework 8.1

print("The mood checker")
mood= input("Mood checking: ")
if mood == "happy":
    print ("It is great to see you happy!")
elif mood == "nervous":
    print ("Take a deep breath three times.")
elif mood == "sad":
    print("Cheer up!")
elif mood == "excited":
    print("Enjoy!")
elif mood == "relaxed":
    print("Cool!")
else:
    print("I don't recognize this mood")

# homework 8.2

print("Guess the secret number")
secret = 781
guess = int(input("Guess number from 1 to 1000: "))

if guess == secret:
    print("Congratulations!")
else:
    print("Better luck next time!")

# homework 8.3

print("calculator")
x = int(input("Vpiši prvo število: "))
y = int(input("Vpiši drugo število:  "))
operation = input("vpiši operacijo +,-,* ali/: ")
if operation == "+":
    print (x + y)
elif operation == "-":
    print (x - y)
elif operation == "*":
    print (x * y)
elif operation == "/":
    print (x / y)
else:
    print("operacija ne obstaja")