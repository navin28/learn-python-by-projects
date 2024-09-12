def quizgame():
    print("Let's play")
    
    score = 0
    
    question1 = input("What is abbrevation of RAM?\n")
    if question1.lower() == "random access memory":
        score += 1
        print("Correct!!!")
    else:
        print("WRONG")
        
    question2 = input("What is the abbrevation of CPU?\n")
    if question2.lower() == "central processing unit":
        score += 1
        print("Correct!!!")
    else:
        print("WRONG")
    
    question3 = input("What is the abbrevation of ROM?")
    if question3.lower() == "read only memory":
        score += 1
        print("Correct!!!")
    else:
        print("WRONG")
    question4 = input("What is the abbrevation of GPU?\n")
    if question4.lower() == "graphical processing unit":
        score += 1
        print("Correct!!!")
    else:
        print("WRONG")
    
    print("you got " + str(score) + " questions correct out of 4")
    print("you got " + str((score/4) * 100) + "%" )
        

playing = input("Are you ready play quiz game? say yes or no\n.")

if playing.lower() != "yes":
    print("Okay!,See you next time")
    quit()
else:
    quizgame()