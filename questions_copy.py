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
    qnlist= (qn1, qn2, qn3, qn4, qn5, qn6, qn7, qn8, qn9, qn10)
    shufflist= list(qnlist)
    random.shuffle(shufflist)
    try:
        if(qn1 == 6000): #Reminder to use == instead of = for "Is equal to"
            print("Question 1 was answered correctly.")
        else: 
            print("Question 1 was answered incorrectly.")
    except:
        print("The input in Question 1 was invalid.")

    qn2= input(f"What is the longest river in the world? (Nile, Yangtze, Amazon, Jordan): ")
    try:    
            if(qn2 == "Nile"): 
                print("Question 2 was answered correctly.")
            else: 
                print("Question 2 was answered incorrectly.")
    except:
            print("The input in Question 2 was invalid.")

    qn3= input(f"Which of the following is the largest continent in the world?(Asia, Africa, Europe, North America): ")
    try:
            if(qn3 == "Asia"): 
                print("Question 3 was answered correctly.")
            else: 
                print("Question 3 was answered incorrectly.")
    except:
            print("The input in Question 3 was invalid.")

    qn4= input(f"What is the fastest land animal? (Cheetah, Cobra, Leopard, Gazelle): ")
    try:
            if(qn4 == "Cheetah"): 
                print("Question 4 was answered correctly.")
            else: 
                print("Question 4 was answered incorrectly.")
    except:
            print("The input in Question 4 was invalid.")

    qn5= input(f"What is the largest mammal in the world?(African Elephant, Blue Whale, Hippopotamus, Giraffe): ")
    try:
            if(qn5 == "Blue Whale"): 
                print("Question 5 was answered correctly.")
            else: 
                print("Question 5 was answered incorrectly.")
    except:
            print("The input in Question 5 was invalid.")

    qn6= int(input(f"5 + 5 (9, 50, 55, 10): "))
    try:
            if(qn6 == 10): 
                print("Question 6 was answered correctly.")
            else: 
                print("Question 6 was answered incorrectly.")
    except:
            print("The input in Question 6 was invalid.")

    qn7= int(input(f"19 + 17 (36, 38, 42, 39): "))
    try:
            if(qn7 == 38): 
                print("Question 7 was answered correctly.")
            else: 
                print("Question 7 was answered incorrectly.")
    except:
            print("The input in Question 7 was invalid.")

    qn8= int(input(f"38 + 42 (70, 80, 90, 100): "))
    try:
            if(qn8 == 80): 
                print("Question 8 was answered correctly.")
            else: 
                print("Question 8 was answered incorrectly.")
    except:
            print("The input in Question 8 was invalid.")

    qn9= int(input(f"90 + 95 (195, 185, 175, 165): "))
    try:
            if(qn9 == 185): 
                print("Question 9 was answered correctly.")
            else: 
                print("Question 9 was answered incorrectly.")
    except:
            print("The input in Question 9 was invalid.")

    qn10= int(input(f"16 + 66 (86, 82, 76, 98): "))
    try:
            if(qn10 == 82): 
                print("Question 10 was answered correctly.")
            else: 
                print("Question 10 was answered incorrectly.")
    except:
            print("The input in Question 10 was invalid.")
     
    qnlist= (qn1, qn2, qn3, qn4, qn5, qn6, qn7, qn8, qn9, qn10)
    shufflist= list(qnlist)
    random.shuffle(shufflist)

test()
