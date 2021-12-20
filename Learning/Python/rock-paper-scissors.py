#!/bin/python3


class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
        self.gamesWon = 0
        self.choices = ["rock", "paper", "scissors", "lizard", "spock"]

    def choose(self):
        self.choice = input(f"{self.name}, select from {', '.join(self.choices)} >> ")
        while not self.choice in self.choices:
            self.choice = input(
                f"{self.name}, select from {', '.join(self.choices)} >> "
            )

        print(f"{self.name} chooses {self.choice}")

    def toNumericalChoice(self):
        switcher = {"rock": 0, "paper": 1, "scissor": 2, "lizard": 3, "spock": 4}
        return switcher[self.choice]

    def incrementPoint(self):
        self.points += 1


class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0],
        ]

        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print(f"Round resulted in {self.getResultAsString(result)}")

        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultAsString(self, result):
        res = {0: "draw", 1: "win", -1: "loss"}

        return res[result]

    def awardPoints(self):
        print("implement later")


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Player 1")
        self.secondParticipant = Participant("Player 2")

    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

        game_round = GameRound(self.participant, self.secondParticipant)

    def checkEndCondition(self):
        print("implement later")

    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = f"Winner is {self.participant.name}"
        elif self.participant.points < self.secondParticipant.points:
            resultString = f"Winner is {self.secondParticipant.name}"
        print(resultString)

    def checkEndCondition(self):
        answer = input("Continue game y/n")
        if answer == "y":
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print(
                f"Game over, {self.participant.name} has {self.particpant.points}, and {self.secondParticipant.name} has {self.secondParticipant.points}"
            )


game = Game()

game.start()
