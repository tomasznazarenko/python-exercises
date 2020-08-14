from random import choice


def get_option():
    return input('Type "play" to play the game, "exit" to quit: ')


def main():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word = choice(word_list)
    hint = "-" * (len(word))
    attempts = 8
    typed_letters = set()

    print("H A N G M A N")

    while True:
        print(hint)

        letter = input("Input a letter: ")

        if letter in typed_letters:
            print("You already typed this letter")
            print()
            continue
        elif len(letter) != 1:
            print("You should input a single letter")
            print()
            continue
        elif not (letter.islower() and letter.isascii()):
            print("It is not an ASCII lowercase letter")
            print()
            continue
        else:
            typed_letters.add(letter)

        if letter in hint:
            print("No improvements")
            attempts -= 1
        elif letter in word:
            indices = [index for index, element in enumerate(word) if element == letter]
            for index in indices:
                hint = hint[:index] + letter + hint[index+1:]
        else:
            print("No such letter in the word")
            attempts -= 1

        if attempts == 0 and hint != word:
            print("You are hanged!")
            print()
            break
        elif attempts >= 0 and hint == word:
            print("You guessed the word!")
            print("You survived!")
            print()
            break
        else:
            print()


while get_option() == "play":
    main()
