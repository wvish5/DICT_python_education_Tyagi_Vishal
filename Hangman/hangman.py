# Этап 1
print("HANGMAN")
print("The game will be available soon.")
# Этап 2
word = "python"
a = input()
if word == a:
    print("You survived!")
else:
    print("You lost!")
# Этап 3
words = ['python', 'java', 'php', 'javascript']
import random

q = random.choice(words)
if a == q:
    print("You survived!")
else:
    print("You lost!")
# Этап 4
ln = len(q) - 2
print(q[0:2] + "-" * ln)
a = input()
if a == q:
    print("You survived!")
else:
    print("You lost!")
# Этап 5
ln = len(word)
split = list(word)
guess = ["-" for i in split]
print("-" * ln)
for i in range(8):
    print("input a letter:")
    a = input()
    if a in split:
        for i, c in enumerate(split):
            if c == a:
                guess[i] = a
                print(*guess, sep="")
        if "-" not in guess:
            print("Thanks for playing!\nWe'll see how well you did in the next stage")
# Этап 6
print("Guess the word:)")
attempt = 8
while attempt != 0:
    print("input a letter:")
    a = input()
    if a in split and a not in guess:
        for i, c in enumerate(split):
            if c == a:
                guess[i] = a
                print(*guess, sep="")

    elif a in guess:
        print("No improvements")
        attempt -= 1
    else:
        print("That letter doesn't appear in the word")
        attempt -= 1
if "-" not in guess:
    print("You guessed the word!\nYou survived!")
else:
    print("You lost!")
