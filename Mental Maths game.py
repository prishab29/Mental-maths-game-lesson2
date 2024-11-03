import random
a = int(input("Choose an operation to practice:\nAddition'1'\nSubtraction'2'\nMultiplication'3'\nDivision'4'\nYour choice(in number): "))
#This is for the code to take in the users choice of operation
b = int(input("Choose a difficulty level:\nEasy'1'\nMedium'2'\nHard'3'\nYour choice(in number): "))
#This is for the code to take in the users choice of level of difficiutly
score = 0
#This is for the user to see their score out of 20 at the end
aq = set()
#Set to avoid repeat in equations adn keeps track of all the equations asked so far by the code
if b == 1:  # Easy
    r = range(0, 21)
elif b == 2:  # Medium
    r = range(0, 50)
else:  # Hard
#These are the ranges for different difficulty levels
    r = range(0, 100)
if a==3 and b==1:
    n= range(1, 10)
elif a==3 and b==2:
    n= range (1, 15)
else:
    n= range (1, 25)
#These are different ranges for multiplication, as it is harder to do with even a small range of numbers.
if a == 1 and b == 1:
#This is for when the user chooses addition and level easy
    for i in range(1, 21):
    #Range is used so that there are 20 questions
        # The loop below is used to ensure that no equations are repeated
        while True:
            #These are the random generated numbers for the questions
            d= random.choice(r)
            e= random.choice(r)
            # Makes sure the  the question pair is in a consistent order (smallest first),
            #so (d, e) and (e, d) are treated as the same question and won't appear twice to the user
            q = (d, e) if d <= e else (e, d)
             # Checks if a question pair has already been used, and if so adds another question to the set 'q' to mark it as used
            if q not in aq:
                #Adds another question to the set 'q' to mark it as used
                aq.add(q)# Adds a question to the set 'q' if a question h
                # Breaks out of the loop preventing the creation of duplicate questions in the next repetition
                break # Exit the loop once a unique question is found
        
            
        a1= input(f"Q{i}){d}+{e}: ")
        if a1=="":
        # Check if the input is empty; if so, it's invalid
            print("INVALID INPUT(This is counted as a question in your score)")  # Inform the user of invalid input
            #so int() raises a ValueError when the value is not correct so you can catch it and do something
            #exit(1) means exit the program but return an error
        #Converts the users input to float(decimal) to ensure it is a valid input
        try:
            a1=int(a1)
            
       
        except ValueError:
            print ("INVALID INPUT(This is counted as a question in your score)")
        if a1 == d+e:
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        else:
             #This is what the code outputs if the users answer is wrong
            print ("Wrong ✘, Correct answer is:",d+e)
    print("Your score is:", score, "out of 20")
        
elif a==1 and b==2:
#This is for when the user chooses addition and level medium
    for o in range (1, 21):
    #Range is used so that there are 20 questions
        while True:
            #These are the random generated numbers for the questions
            d= random.choice(r)
            e= random.choice(r)
            q= (d, e) if d <= e else (e, d)
            if q not in aq:
                aq.add(q)
                break
            
        a2= input(f"Q{o1}){d}+{e}: ")
        if a2=="":
        # Check if the input is empty; if so, it's invalid
            print("INVALID INPUT(This is counted as a question in your score)")  # Inform the user of invalid input
            
            
        
        try:
            a2=int(a2)
            
       
        except ValueError:
            print ("INVALID INPUT(This is counted as a question in your score)")
        if a2 == d+e:
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        else:
             #This is what the code outputs if the users answer is wrong
            print ("Wrong ✘, Correct answer is:",d+e)
    print("Your score is:", score, "out of 20")
elif a==1 and b==3:
#This is for when the user chooses addition and level hard
    for p in range(1, 21):
    #Range is used so that there are 20 questions
        while True:
            #These are the random generated numbers for the questions
            d= random.choice(r)
            e= random.choice(r)
            q = (d, e) if d <= e else (e, d)
            if q not in aq:
                aq.add(q)
                break
            
        a3= input(f"Q{p}){d}+{e}: ")
        if a3=="":
        # Check if the input is empty; if so, it's invalid
            print("INVALID INPUT(This is counted as a question in your score)")  # Inform the user of invalid input
            
            
        
        try:
            a3=int(a3)
            
       
        except ValueError:
            print ("INVALID INPUT(This is counted as a question in your score)")
        if a3 == d+e:
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        else:
            #This is what the code outputs if the users answer is wrong
            print ("Wrong ✘, Correct answer is:",d+e)
    print("Your score is:", score, "out of 20")
    
elif a==2 and b==1:
#This is for when the user chooses subtraction and level easy
    for i in range (1, 21):
    #Range is used so that there are 20 questions
        while True:
            #These are the random generated numbers for the questions
            d= random.choice(r)
            e= random.choice(r)
            q = (d, e) if d <= e else (e, d)
            if q not in aq:
                aq.add(q)
                break
            
        s1= input(f"Q{i}){d}-{e}: ")
        if s1=="":
        # Check if the input is empty; if so, it's invalid
            print("INVALID INPUT(This is counted as a question in your score)")  # Inform the user of invalid input
            
            
        
        try:
            s1=int(s1)
            
       
        except ValueError:
            print ("INVALID INPUT(This is counted as a question in your score)")
        if s1 == d-e:
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        else:
            #This is what the code outputs if the users answer is wrong
            print ("Wrong ✘, Correct answer is:",d-e)
    print("Your score is:", score, "out of 20")
elif a==2 and b==2:
#This is for when the user chooses subtraction and level medium
    for o in range (1, 21):
    #Range is used so that there are 20 questions (it goes from 1-21 as it is unlikely to have a question zero)
        while True:
            #These are the random generated numbers for the questions
            d= random.choice(r)
            e= random.choice(r)
            q = (d, e) if d <= e else (e, d)
            if q not in aq:
                aq.add(q)
                break
            
        s2= input(f"Q{o}){d}-{e}: ")
        if s2=="":
        # Check if the input is empty; if so, it's invalid
            print("INVALID INPUT(This is counted as a question in your score)")  # Inform the user of invalid input
            
            
        
        try:
            s2=int(s2)
            
       
        except ValueError:
            print ("INVALID INPUT(This is counted as a question in your score)")
        if s2 == d-e:
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        else:
            #This is what the code outputs if the users answer is wrong
            print ("Wrong ✘, Correct answer is:",d-e)
    print("Your score is:", score, "out of 20")
elif a==2 and b==3:
#This is for when the user chooses subtraction and level hard
    for p in range (1, 21):
    #Range is used so that there are 20 questions
        while True:
            #These are the random generated numbers for the questions
            d= random.choice(r)
            e= random.choice(r)
            q = (d, e) if d <= e else (e, d)
            if q not in aq:
                aq.add(q)
                break
            
        s3= input(f"Q{p}){d}-{e}: ")
        if s3=="":
        # Check if the input is empty; if so, it's invalid
            print("INVALID INPUT(This is counted as a question in your score)")  # Inform the user of invalid input
            
            
        
        try:
            s3=int(s3)
            
       
        except ValueError:
            print ("INVALID INPUT(This is counted as a question in your score)")
        if s3 == d-e:
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        else:
            #This is what the code outputs if the users answer is wrong
            print ("Wrong ✘, Correct answer is:",d-e)
    print("Your score is:", score, "out of 20")
elif a==3 and b==1:
#This is for when the user chooses multiplication and level easy
    for i in range (1, 21):
        while True:
            #These are the random generated numbers for the questions
            d= random.choice(n)
            e= random.choice(n)
            q = (d, e) if d <= e else (e, d)
            if q not in aq:
                aq.add(q)
                break
            
        m1= input(f"Q{i}){d}x{e}: ")
        if m1=="":
        # Check if the input is empty; if so, it's invalid
            print("INVALID INPUT(This is counted as a question in your score)")  # Inform the user of invalid input
            
            
        
        try:
            m1=int(m1)
            
       
        except ValueError:
            print ("INVALID INPUT(This is counted as a question in your score)")
        if m1== d*e:
            print ("Correct ✔")
            score += 1
        else:
            print ("Wrong ✘, Correct answer is:",d*e)
    print ("Your score is:", score, "out of 20")
elif a==3 and b==2:
#This is for when the user chooses multiplication and level medium
    for o in range (1, 21):
    #Range is used so that there are 20 questions
        while True:
            #These are the random generated numbers for the questions
            d= random.choice(n)
            e= random.choice(n)
            q = (d, e) if d <= e else (e, d)
            if q not in aq:
                aq.add(q)
                break
            
        m2= input(f"Q{o}){d}x{e}: ")
        if m2=="":
        # Check if the input is empty; if so, it's invalid
            print("INVALID INPUT(This is counted as a question in your score)")  # Inform the user of invalid input
            
            
        
        try:
            m2=int(m2)
            
       
        except ValueError:
            print ("INVALID INPUT(This is counted as a question in your score)")
        if m2 == d*e:
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        else:
            #This is what the code outputs if the users answer is wrong
            print ("Wrong ✘, Correct answer is:",d*e)
    print("Your score is:", score, "out of ")
elif a==3 and b==3:
#This is for when the user chooses multiplication and level hard
    for p in range (1, 21):
    #Range is used so that there are 20 questions
        while True:
            #These are the random generated numbers for the questions
            d= random.choice(n)
            e= random.choice(n)
            q = (d, e) if d <= e else (e, d)
            if q not in aq:
                aq.add(q)
                break
            
        m3= input(f"Q{p}){d}x{e}: ")
        if m3=="":
        # Check if the input is empty; if so, it's invalid
            print("INVALID INPUT(This is counted as a question in your score)")  # Inform the user of invalid input
            
            
        
        try:
            m3=int(m3)
            
       
        except ValueError:
            print ("INVALID INPUT(This is counted as a question in your score)")
        if m3 == d*e:
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        else:
            #This is what the code outputs if the users answer is wrong
            print ("Wrong ✘, Correct answer is:",d*e)
    print("Your score is:", score, "out of 20")
elif a==4 and b==1:
    print ("When you answer these questions remember to ROUND your answer to 2 DECIMAL PLACES")
#This is for when the user chooses division and level easy
    for i in range (1, 21):
    #Range is used so that there are 20 questions
        while True:
            #These are the random generated numbers for the questions
            d= random.choice(r)
            e= random.choice(r)
            q = (d, e) if d <= e else (e, d)
            if q not in aq:
                aq.add(q)
                break
            
        d1= input(f"Q{i}){d}÷{e}: ").strip()
        if d1=="":
        # Check if the input is empty; if so, it's invalid
            print("INVALID INPUT(This is counted as a question in your score)")  # Inform the user of invalid input
            
            
        
        try:
            d1=float(d1)
            
       
        except ValueError:
            print ("INVALID INPUT(This is counted as a question in your score)")
        if d1 == round(d / e, 2):
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        elif d1 == "":
            print ("INVALID INPUT, Please start the game again")
        else:
            #This is what the code outputs if the users answer is wrong
            print("Wrong ✘, Correct answer is:", round(d / e, 2))
    print("Your score is:", score, "out of 20")
elif a==4 and b==2:
    print ("When you answer these questions remember to ROUND your answer to 2 DECIMAL PLACES")
#This is for when the user chooses division and level easy
    for o in range (1, 21):
    #Range is used so that there are 20 questions
        while True:
            #These are the random generated numbers for the questions
            d= random.choice(r)
            e= random.choice(r)
            q = (d, e) if d <= e else (e, d)
            if q not in aq:
                aq.add(q)
                break
            
        d2= input(f"Q{o}){d}÷{e}: ").strip()
        if d2=="":
        # Check if the input is empty; if so, it's invalid
            print("INVALID INPUT(This is counted as a question in your score)")  # Inform the user of invalid input
            
            
        
        try:
            d2=float(d2)
            
       
        except ValueError:
            print ("INVALID INPUT(This is counted as a question in your score)")
        if d2 == round(d / e, 2):
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        else:
            #This is what the code outputs if the users answer is wrong
            print("Wrong ✘, Correct answer is:", round(d / e, 2))
    print("Your score is:", score, "out of 20")
elif a==4 and b==3:
    print ("When you answer these questions remember to ROUND your answer to 2 DECIMAL PLACES")
#This is for when the user chooses division and level easy
    for p in range (1, 21):
    #Range is used so that there are 20 questions
        while True:
            #These are the random generated numbers for the questions
            d= random.choice(r)
            e= random.choice(r)
            q = (d, e) if d <= e else (e, d)
            if q not in aq:
                aq.add(q)
                break
             
        d3 = input(f"Q{p}){d}÷{e}: ").strip()
        if d3=="":
        # Check if the input is empty; if so, it's invalid
            print("INVALID INPUT(This is counted as a question in your score)")  # Inform the user of invalid input
            
            
        
        try:
            d3=float(d3)
            
       
        except ValueError:
            print ("INVALID INPUT(This is counted as a question in your score)")
            
        if d3 == round(d / e, 2):
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        else:
            #This is what the code outputs if the users answer is wrong
            print("Wrong ✘, Correct answer is:", round(d / e, 2))
    print("Your score is:", score, "out of 20") 
else:
    print ("INVALID INPUT, Please start the game again")
c=int(input("Choose how you wish to continue:\n﻿﻿Do more questions(1)\nEnd the game(2)\nYour choice(in number):"))
if c==1:
   print("Press the green play button at the top")
   print("THANK YOU FOR PLAYING\n👋BYE!")
elif c==2:
    print("THANK YOU FOR PLAYING\n👋BYE!")
elif c!=1 or c!= 2:
    print ("INVALID INPUT👋")