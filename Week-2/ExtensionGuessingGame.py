import random as R
print("Enter a number between 1 and 10 (inclusive): ")
GuessedNum = int(input())
RandomNumber = R.randint(1, 11)
print("The random number was: " + str(RandomNumber))
print(str(RandomNumber == GuessedNum))
print("This is a test")
