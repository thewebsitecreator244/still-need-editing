import random

bet = 67676766
playagain = "y"
#"suiiiiiiiiiiiiiiiiiiiii and suuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuus"
money = 250
moneywon = 0
moneylost = 0
print("welcome to blackjack♠️♦️")
while playagain == "y":
    ebet = random.randint(1, 250)
    while not bet <= money:
        print(f"you have {money}$ you won {moneywon}$ and lost {moneylost}$")
        bet = int(input("how much do you want to bet: "))
        if bet > money:
            print("too much")
        else:
            if bet == money:
                print("all in")
        print(f"cpu bet {ebet}")
    YourStartCard = random.randint(1, 21)
    CpuStartCard = random.randint(1, 21)
    print(f"your cards make up {YourStartCard}")
    print(f"cpu cards make {CpuStartCard}")
    if YourStartCard == 21:
        print("blackjack")
        money += ebet
        moneywon += ebet
        bet = 67676766
        playagain = input("do you want to play again y/n: ")
    elif CpuStartCard == 21:
        print("cpu got blackjack")
        money -= bet
        moneylost += bet
        bet = 67676766
        playagain = input("do you want to play again y/n: ")
    elif YourStartCard == 21 and CpuStartCard == 21:
        print("dealer wins")
        money -= bet
        moneylost += bet
        bet = 67676766
        playagain = input("do you want to play again y/n: ")
    elif YourStartCard < 21 and CpuStartCard < 21:
        print("you can hit or stand")
        hitstand = input("hit or stand: ")
        if hitstand == "hit":
            YourStartCard += random.randint(1, 11)
            print(f"your cards make up {YourStartCard}")
        elif hitstand == "stand":
            CpuStartCard += random.randint(1, 11)
            print(f"cpu cards make up {CpuStartCard}")
        cpuhitstandchoicelist = ["hit", "stand"]
        cpuhitstandchoice = random.choice(cpuhitstandchoicelist)
        if random.randint(0, 2) == 1:
            if cpuhitstandchoice == "hit":
                print("cpu hit")
                CpuStartCard += random.randint(1, 11)
                print(f"cpu cards make up {CpuStartCard}")
            elif cpuhitstandchoice == "stand":
                print("cpu stand")
                YourStartCard += random.randint(1, 11)
                print(f"your cards make up {YourStartCard}")
    if YourStartCard > 21:
        print("you busted")
        money -= bet
        moneylost += bet
        bet = 67676766
        playagain = input("do you want to play again y/n: ")
    if CpuStartCard > 21:
        print("cpu busted")
        money += ebet
        bet = 67676766
        moneywon += ebet
        playagain = input("do you want to play again y/n: ")
