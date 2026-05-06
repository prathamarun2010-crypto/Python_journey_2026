a= int(input("Enter your score: "))


def fetched_stored_highscore():
    with open("highscore.txt", "r") as file:
        return int(file.read())
    
current_highscore = fetched_stored_highscore()

if a > current_highscore:
        with open("highscore.txt", "w") as file:
            file.write(str(a))
        print("Congratulations! You have the new high score!")

elif a == current_highscore:
    print("Congratulations! You have tied the high score!")        

else:
    print(f"The current high score is {current_highscore}. try to aim higher next time!")

fetched_stored_highscore()
