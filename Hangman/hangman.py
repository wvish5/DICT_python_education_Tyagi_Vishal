import random

print("HANGMAN")
print("The game will be available soon.")

wordlist = ['python', 'java', 'javascript', 'php']
randomWord = random.choice(wordlist)

p = input("Введите ваше слово " + str(randomWord[0:3] + '-' * (len(randomWord) - 3)) + ": ")

if randomWord == p:
    print("You survived!")
else:
    print("You lost!")
