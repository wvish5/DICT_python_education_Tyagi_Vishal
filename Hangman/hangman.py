import random
print("HANGMAN")
print("The game will be available soon!")
word = ""
letter = ""
a = input()
def show(letter):
    for a in word:
        print(a)
        for a in letter:
            print(a, end='')
        else:
            print('_', end='')
while True:
    type = input("play or exit:")

    if type == "play":

        words = ['python', 'java', 'javascript', 'php']
        word = random.choice(words)
        letter = 'i'
        wrong = 8
        Win = True
        attempt = 8
        while attempt > 0:
            while True:
                inputletter = ""
                inputletter += input("input a letter")
                if len(inputletter) == 1:
                    if inputletter.islower():
                        if wrong != 1:
                            if inputletter not in letter:
                                if inputletter in word:
                                    letter += inputletter
                                else:
                                    print("Данной буквы нет!")
                                    wrong -= 1
                            for a in word:
                                if a in letter:
                                    Win = True
                                else:
                                    Win = False
                            if Win:
                                print("Вы победили")
                                break
                        else:
                            print("Вы уже вводили эту букву!")
                    else:
                        print('Вы проиграли!')
                        break
                else:
                    print('Введите маленькую букву!')
            else:
                print('Введите одну английскую букву!')
        else:
            print('Wrong command!')
    elif type == 'exit':
        break





















