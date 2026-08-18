import random

# The Coin class simulates a coin that can be flipped 

class Coin:

    # __init__ method initializes the __sideup data attribute with heads

    def __init__(self):
        self.__sideup = 'Heads' # __sideup is a private attribute

    # The toss method generates 0 (heads) or 1 (tails)

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # The get_sideup method returns the value referenced by sideup

    def get_sideup(self):
        return self.__sideup

def main():
    # Create an object from the Coin class
    my_coin = Coin()

    # Display side of coin that is facing up
    print(f'This side is up: {my_coin.get_sideup()}')

    # Toss the coin
    print('I am the tossing the coin...')
    my_coin.toss()

    # Display side of coin that is facing up
    print(f'This side is up: {my_coin.get_sideup()}')  

# Call the main function
if __name__ == '__main__':
    main()  