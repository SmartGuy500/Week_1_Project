"""
The questions: 

What is the temperature of the surface of the sun? (6042, 9000, 6000, 6300)
What is the longest river in the world? (Nile, Yangtze, Amazon, Jordan)
Which of the following is the largest continent in the world?(Asia, Africa, Europe, North America)
What is the fastest land animal? (Cheetah, Cobra, Leopard, Gazelle)
What is the largest mammal in the world?(African Elephant, Blue Whale, Hippopotamus, Giraffe)
5 + 5 (9, 50, 55, 10)
19 + 17 (36, 38, 42, 39)
38 + 42 (70, 80, 90, 100)
90 + 95 (195, 185, 175, 165)
16 + 66 (86, 82, 76, 98)

"""
import random
def test():
   
    
    qn1= int(input(f"What is the temperature of the surface of the sun? (6042, 9000, 6000, 6300): "))
    qn2= input(f"What is the longest river in the world? (Nile, Yangtze, Amazon, Jordan): ")
    qn3= input(f"Which of the following is the largest continent in the world?(Asia, Africa, Europe, North America): ")
    qn4= input(f"What is the fastest land animal? (Cheetah, Cobra, Leopard, Gazelle): ")
    qn5= input(f"What is the largest mammal in the world?(African Elephant, Blue Whale, Hippopotamus, Giraffe): ")
    qn6= int(input(f"5 + 5 (9, 50, 55, 10): "))
    qn7= int(input(f"19 + 17 (36, 38, 42, 39): "))
    qn8= int(input(f"38 + 42 (70, 80, 90, 100): "))
    qn9= int(input(f"90 + 95 (195, 185, 175, 165): "))
    qn10= int(input(f"16 + 66 (86, 82, 76, 98): "))

    score=0

    """
    qnlist= [qn1, qn2, qn3, qn4, qn5, qn6, qn7, qn8, qn9, qn10]
    random.shuffle(qnlist)
    qn1, qn2, qn3, qn4, qn5, qn6, qn7, qn8, qn9, qn10 = qnlist
    """
    try:
        if(qn1 == 6000): #Reminder to use == instead of = for "Is equal to"
            print("Question 1 was answered correctly.")
            score= score + 1
        else: 
            print("Question 1 was answered incorrectly.")
    except:
        print("The input in Question 1 was invalid.")

    
    try:    
        if(qn2 == "Nile" or qn2 == "nile"): #Note that if you dont specify 'or == "nile"' instead of 'or qn2 =="nile"', the output will constantly be a correct
                print("Question 2 was answered correctly.")
                score= score + 1
        else: 
                print("Question 2 was answered incorrectly.")
    except:
            print("The input in Question 2 was invalid.")

    
    try:
            if(qn3 == "Asia" or qn3 == "asia"): 
                print("Question 3 was answered correctly.")
                score= score + 1
            else: 
                print("Question 3 was answered incorrectly.")
    except:
            print("The input in Question 3 was invalid.")


    try:
            if(qn4 == "Cheetah" or qn4 == "cheetah"): 
                print("Question 4 was answered correctly.")
                score= score + 1
            else: 
                print("Question 4 was answered incorrectly.")
    except:
            print("The input in Question 4 was invalid.")


    try:
            if(qn5 == "Blue Whale" or qn5 == "Blue whale" or qn5 == "blue whale"): 
                print("Question 5 was answered correctly.")
                score= score + 1
            else: 
                print("Question 5 was answered incorrectly.")
    except:
            print("The input in Question 5 was invalid.")


    try:
            if(qn6 == 10): 
                print("Question 6 was answered correctly.")
                score= score + 1
            else: 
                print("Question 6 was answered incorrectly.")
    except:
            print("The input in Question 6 was invalid.")


    try:
            if(qn7 == 38): 
                print("Question 7 was answered correctly.")
                score= score + 1
            else: 
                print("Question 7 was answered incorrectly.")
    except:
            print("The input in Question 7 was invalid.")


    try:
            if(qn8 == 80): 
                print("Question 8 was answered correctly.")
                score= score + 1
            else: 
                print("Question 8 was answered incorrectly.")
    except:
            print("The input in Question 8 was invalid.")


    try:
            if(qn9 == 185): 
                print("Question 9 was answered correctly.")
                score= score + 1
            else: 
                print("Question 9 was answered incorrectly.")
    except:
            print("The input in Question 9 was invalid.")


    try:
            if(qn10 == 82): 
                print("Question 10 was answered correctly.")
                score= score + 1
            else: 
                print("Question 10 was answered incorrectly.")
    except:
            print("The input in Question 10 was invalid.")

    print(f"Your score is {score} out of 10")
    try:
        if(score >= 9 and score<=10):
            print("Excellent")
        elif(score >=7 and score < 9): 
            print("Good")
        elif(score >= 5 and score < 7): 
            print("...there's some work to be done")
        else: 
            print("Please attempt the quiz again")      
    except:
          print("Scoring Error")

test()
