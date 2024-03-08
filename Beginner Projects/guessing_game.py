import random
import math

class Guess:
    noOfGuess = 0

    def __init__(self, upper, lower):
        self.noOfGuess = round(math.log2(upper - lower + 1))

    def is_correct(self, num):
        while self.noOfGuess >= 1:
            guess = int(input("Guess the number from " + str(lower) + " to " + str(upper) + ": "))
            self.noOfGuess -= 1

            if guess > upper or guess < lower:
                self.noOfGuess +=1
                print("\nPlease guess a number within the range of " + str(lower) + " to " + str(upper) + 
                      ". You're left with " + str(self.noOfGuess) + " guesses.")
                continue

            if guess == num:
                return "You guessed the right  number i.e. " + str(num)
            elif guess > num:
                print("\nYour guess is too big. You're left with " + str(self.noOfGuess) + " guesses.")
            else:
                print("\nYour guess is too small. You're left with " + str(self.noOfGuess) + " guesses.")
        return "You haven't guess the number within max guesses. The number was " + str(num) + "."

if __name__ == "__main__":
    lower = int(input("Enter lower bound "))
    upper = int(input("Enter upper bound "))

    num = random.randrange(lower, upper, 1)

    guess = Guess(upper, lower)

    print(guess.is_correct(num))
