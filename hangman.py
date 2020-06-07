import random
f = open("randwords.txt")
a = f.readlines()

def hangman():
    global word
    word = random.choice(a) 
    word = word[:-1]
    used = []
    progress = []
    for p in range(len(word)):
        c = " _ "
        progress.append(c)
    attempts = 9
    global final
    final = len(used)
    while c in progress:
        guess = input("Guess a letter: ").lower() 
        if guess in word: 
            number = str(word.count(guess)) 
            print ("Nice! The letter, " + str(guess) + ", is in the word " + number + " times.")    
            for g in range(len(word)):
                if guess in word[g]:
                    progress[g] = guess
                    final += 1
                else:
                    None
            used.append(guess)
            print (progress)
            print ("Your guesses: " + str(used) + '\n')
        else:
            attempts = attempts - 1
            final += 1
            used.append(guess)
            print ("Nope, you have " + str(attempts) + " tries left.")
            print (progress)
            print ("Your guesses: " + str(used))
        if attempts == 0:
            print ("YOU DIED")
            print ("The word was " + word.upper() + ".")
            quit()


print ("Welcome to Hangman! Enter 'START' to begin game.")

x = input().upper()

if x == "START":
    hangman()
else:
    print ("Please follow the instructions!")

print ("Congratulations, the word was " + word.upper())
print ("It only took you " + str(final) + " guesses!")
