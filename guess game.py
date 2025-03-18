from breezypythongui import EasyFrame
import random


class GuessingGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Guessing Game")
        self.setSize(350, 200)
        self.setResizable(False)

        self.myNumber = random.randint(1, 100)
        self.count = 0

        self.addLabel(text="Guess a number between 1 and 100:", row=0, column=0, columnspan=2, sticky="NSEW")

        self.inputField = self.addIntegerField(value=0, row=1, column=0, sticky="EW")

        self.addButton(text="Guess", row=1, column=1, command=self.guess_number)
        self.addButton(text="Reset", row=2, column=1, command=self.reset_game)

        self.resultLabel = self.addLabel(text="Start guessing!", row=3, column=0, columnspan=2, sticky="NSEW")

    def guess_number(self):
        self.count += 1
        guess = self.inputField.getNumber()

        if guess < self.myNumber:
            message = "Try Higher!"
        elif guess > self.myNumber:
            message = "Try Lower!"
        else:
            message = f"🎉 Congratulations! You guessed it in {self.count} tries!"
            self.reset_game()

        self.resultLabel['text'] = message
        self.inputField.setNumber(0)  # Clear input field

    def reset_game(self):
        self.myNumber = random.randint(1, 100)
        self.count = 0
        self.resultLabel['text'] = "Game reset! Start guessing!"
        self.inputField.setNumber(0)


if __name__ == "__main__":
    GuessingGame().mainloop()
