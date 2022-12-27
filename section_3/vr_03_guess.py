# guess game

from random import randint

number = int(input("Digite um número\n"))

result = randint(1, 5)

if number == result:
    print("Congratulations, you got it right!")
else:
    print(f"You missed. The number drawn was: {result}")
