#I added more options for the user to choose

user_choice = input("What happened?! You were reading an strange old book and now, suddenly, you are in ancient China. There is a small town nearby...\n\nWhat do you want to do? EXPLORE // RUNAWAY // RETURN\n")

if user_choice == "explore":
    strange_town = input("The town is full of all kinds of people. Some groups of strangers are coming to you. What are you gonna do?\n\nCHAT // FIGHT // ESCAPE\n")
    if strange_town == "chat":
        print("After a little conversation, you find that the people are very nice. Maybe you should look for a house to rent here...\n\nGAME OVER")
    elif strange_town == "fight":
        print("You don't have any chance of winning... they kick you out of town. You will return home with some injuries and a lesson: you should be nicer to strangers!\n\nGAME OVER")
    elif strange_town == "escape":
        print("You escape out of town and see a cave on the side of the mountain. Yes, you escaped, but you are not a coward! It's time to explore again!\n\nThe dragon inside the cave is not a fan of curious persons who arrive without invitation.\n\nGAME OVER")
    
elif user_choice == "runaway":
    dragon_cave = input("You escape far away from the town and see a cave on the side of the mountain. It looks like a quiet place to rest...\n\n But the dragon inside the cave is not a fan of curious persons who arrive without invitation.\n\nHe looks angry. There are some objects on the cave floor. Which one will you choose? SWORD // BOOK\n")
    if dragon_cave == "sword":
        print("You took the sword! You are ready to fight! But the big dragon eats you immediately. Everyone in the town talks about the visitor who was not kind.\n\nGAME OVER")
    elif dragon_cave == "book":
        print("You start reading... it sounds like an old poem. The dragon is listening and he likes it! You have an unexpected new friend.\n\nEverything is possible with a good book.\n\nGAME OVER")
    else:
        print("I don't understand your choice. Come back when you are ready to be clear.")

elif user_choice == "return":
    print("You are safe and sound back in the library. There is a long and boring day ahead...\n\nGAME OVER")
    
else:
    print("I don't understand your choice. Come back when you are ready to be clear.")
    
