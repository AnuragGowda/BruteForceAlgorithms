from string import printable, whitespace
from time import time
from datetime import timedelta

one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen = [None]*15
allWheels = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen]

class Wheel:
    wheels = []

    def __init__(self, info):
        self.info = [i for i in info]
        self.pos = 0
        self.max = False
        Wheel.wheels.append(self)
        self.location = Wheel.wheels.index(self)
        print('Wheel '+str(self.location+1)+' added')

    @property
    def value(self):
        return self.info[self.pos]

    def turn(self):
        self.pos+=1
        self.max = True if self.pos > len(self.info)-1 else False
        if self.max:
            if self.location != len(Wheel.wheels)-1:
                self.pos = 0
                Wheel.wheels[self.location+1].turn()
            else:
                print('Adding a wheel...')
                self.pos = 0
                allWheels[self.location+1] = Wheel(printable.replace(whitespace,' '))
                
def display(startTime, tries):
    endTime = time() 
    print("It took me " + str(tries)+" tries and "+ str(timedelta(seconds = (endTime - startTime)))+" seconds to brute force your password")
    exit()    

def HackPass(password='123'):
    startTime, tries = time(), 0
    one = Wheel(printable.replace(whitespace,' '))
    while True:
        tries += 1
        blah = display(startTime, tries) if ''.join([str(i.value) for i in Wheel.wheels]) == password else Wheel.wheels[0].turn()

if __name__ == '__main__':
    HackPass()
