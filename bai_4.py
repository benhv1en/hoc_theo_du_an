import random


def IsDraw(human, computer) -> bool:
    return human == computer


def IsWin(human, computer) -> bool:
    return (
        (human == "Keo" and computer == "Bao")
        or (human == "Bua" and computer == "Keo")
        or (human == "Bao" and computer == "Bua")
    )


def IsLost(human, computer) -> bool:
    return (
        (computer == "Keo" and human == "Bao")
        or (computer == "Bua" and human == "Keo")
        or (computer == "Bao" and human == "Bua")
    )


if "__main__" == __name__:
    time = int(input("con giời muốn chơi bao nhiêu lần?: "))
    human_score = 0
    computer_score = 0
    for i in range(0, time):
        human = input("Keo? Bua? Bao?: ")
        computer = random.choice(["Keo", "Bua", "Bao"])
        print("Human: \n", human)
        print("Computer: \n", computer)
        if IsDraw(human, computer):
            print("Hoa")
            human_score += 0.5
            computer_score += 0.5
        elif IsWin(human, computer):
            print("Thang")
            human_score += 1
        else:
            print("Thua")
            computer_score += 1
    f = open("ket_qua_game.txt", "w")
    f.write("Ti so tran dau: \n")
    f.write("\tYou: %.1f\n" % human_score)
    f.write("\tComputer: %.1f\n" % computer_score)
    f.close()
