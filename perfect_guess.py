import random

class perfectguessgame:

    def __init__(self):
        self.attempts = 0
        self.target = random.randint(1, 100)
        self._user_guess = None

    @property
    def user_guess(self):
        return self._user_guess
    
    @user_guess.setter
    def user_guess(self, value):
        if not isinstance(value, int):
            print("value error")
        elif value <1 or value > 100:
            print("Out-off-bounds error")
        else:
            self._user_guess = value
                    
    def play(self):
        while True: 
            user_input= int(input("enter your number: "))
            self.user_guess = user_input
            if self.user_guess != user_input:
                continue
            self.attempts +=1
            if self.user_guess  == self.target:
                print(f"you guess {self.target}  in {self.attempts} number of guesses.")
                break
            elif self.user_guess  < self.target:
                print("aim higher")
            elif self.user_guess > self.target:
                print("aim lower")


game= perfectguessgame()
game.play()

        







        
      