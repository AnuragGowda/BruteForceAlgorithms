# Import everything that we need
from math import trunc
from time import time
from string import printable, whitespace

# Create a display function that will show us the speed of the brute force, after it does this, we will simply exit the program
def display(startTime, tries):
    endTime = time()
    TotalTime = endTime - startTime  
    print("It took me " + str(tries)+" tries and "+ str(TotalTime)+" seconds to brute force your password")
    exit()

# I decided to make this a function so that I could execute it multiple times in the shell, and it also looks neater
def HackPwd(Known=False, password='123'):
    '''
    So the logic for this function is pretty simple but it looks very complicated especially at the bottom with the line: guess.append(possible_chars[(trunc(i/(len(possible_chars)**times)))%len(possible_chars)])
    Heres what actually happens... So for example, if we were only looking at a numerical password with ab and c, so possible_chars would be equal to '0123456789abc', and we didn't know the password length, you would think the program would
    start with 0, then go to 1, then 2, then 3, and so forth. When it reaches c, it will go to 00, then 01, 02 up until 0c, upon which it will go to 10, then 11, 12, all the way to 1c. Next it will go to 20, eventually it would 
    reach cc, and then reset to 000, then 100, and so on so forth. However, my program works in the reverse order, when reacing 9 it will go to 00 then 10, 20, so everything is in a sense flipped. In the code below, I tried to change it
    to how you would think it would work, by changing append(item) to insert(0, item), but that made cracking the password 999 go from taking about .29 seconds to about .32, which is a huge difference when cracking larger passwords. I
    also noticed this with math.trunc() vs int(), the latter causing a similar delay.
    '''

    # Set up variables that we will need
    guess, tries = [], 0

    # Contains all printable letters, numbers, symbols based of ascii, including the space character excluding all other whitespace such as newline, carriage feed, etc. 
    # I would simply replace what this includes if I know that the password would be only alpha-numeric or something
    possible_chars = printable.replace(whitespace,' ')

    # Now we actually begin the brute force, so we start the timer
    startTime = time()
    # Start with guessing a password length of 1, and increase up until 20
    for numb in range(1,21):
        # Set the password length to what we got from the loop above if we don't know the length, otherwise, set it to the length of the password
        password_length = numb if not Known else len(password)
        # Now that we have the size of the password, we actually have to create our guess
        for i in range(len(possible_chars)**password_length): 
            # Increment the tries
            tries += 1 
            # Another loop that helps in creating the guess
            for times in range(password_length):
                # The part where we actually form the guess
                #guess.insert(0, possible_chars[(trunc(i/(len(possible_chars)**times)))%len(possible_chars)])
                guess.append(possible_chars[(trunc(i/(len(possible_chars)**times)))%len(possible_chars)])
            # If we have guessed the password correctly, use our display function to exit, otherwise, we simply reset the guess and keep trying
            guess = display(startTime, tries) if ''.join(guess) == password else []
    
if __name__ == '__main__':
    HackPwd()
