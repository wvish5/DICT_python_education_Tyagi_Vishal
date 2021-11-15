import random

def show(word, letter):
    m = 0
    for i in word:
        if i in letter:
            print(i, end='')
        else:
            print('_', end='')
            m += 1
    return m

wordlist = ['python', 'java', 'javascript', 'php']
n = random.choice(wordlist)
words = ''
attempt = 8

while attempt != 0:
    sum = show(n, words)
    if sum == 0:
        print("\nYou win!")
        break
    p = input(" Guess the letter")
    if len(p) == 1:
        if p.istitle():
            print("Please enter a lowercase English letter")
        else:
            if p in words:
                print("You've already guessed this letter")
            else:
                words += p
            if p not in n:
                print("The letter doesn't appear in the word")
                attempt -= 1
            if attempt == 0:
                print("You loss")
    else:
        print("You should input a single letter")