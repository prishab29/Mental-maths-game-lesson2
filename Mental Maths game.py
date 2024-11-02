import random
a = int(input("Choose an operation to practice:\nAddition'1'\nSubtraction'2'\nMultiplication'3'\nDivision'4'\nYour choice(in number): "))
#This is for the code to take in the users choice of operation
b = int(input("Choose a difficulty level:\nEasy'1'\nMedium'2'\nHard'3'\nYour choice(in number): "))
#This is for the code to take in the users choice of level of difficiutly
score = 0
#This is for the user to see their score out of 20 at the end
q= set()
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
            aq= (d, e) if d <= e else (e, d)
             # Checks if a question pair has already been used, and if so adds another question to the set 'q' to mark it as used
            if aq not in q:
                #Adds another question to the set 'q' to mark it as used
                q.add(aq)# Adds a question to the set 'q' if a question h
                # Breaks out of the loop preventing the creation of duplicate questions in the next repetition
                break # Exit the loop once a unique question is found
        
            
        a1= int(input(f"Q{i}){d}+{e}: "))
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
            aq= (d, e) if d <= e else (e, d)
            if aq not in q:
                q.add(aq)
                break
            
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
            aq= (d, e) if d <= e else (e, d)
            if aq not in q:
                q.add(aq)
                break
            
        a3= int(input(f"Q{p}){d}+{e}: "))
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
            aq= (d, e) if d <= e else (e, d)
            if aq not in q:
                q.add(aq)
                break
            
        s1= int(input(f"Q{i}){d}-{e}: "))
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
            aq= (d, e) if d <= e else (e, d)
            if aq not in q:
                q.add(aq)
                break
            
        s2= int(input(f"Q{o}){d}-{e}: "))
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
            aq= (d, e) if d <= e else (e, d)
            if aq not in q:
                q.add(aq)
                break
            
        s3= int(input(f"Q{p}){d}-{e}: "))
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
            aq= (d, e) if d <= e else (e, d)
            if aq not in q:
                q.add(aq)
                break
            
        m1= int(input(f"Q{i}){d}x{e}: "))
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
            aq= (d, e) if d <= e else (e, d)
            if aq not in q:
                q.add(aq)
                break
            
        m2= int(input(f"Q{o}){d}x{e}: "))
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
            aq= (d, e) if d <= e else (e, d)
            if aq not in q:
                q.add(aq)
                break
            
        m3= int(input(f"Q{p}){d}x{e}: "))
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
            aq= (d, e) if d <= e else (e, d)
            if aq not in q:
                q.add(aq)
                break
            
        d1= float(input(f"Q{i}){d}÷{e}: "))
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
            aq= (d, e) if d <= e else (e, d)
            if aq not in q:
                q.add(aq)
                break
            
        d2= float(input(f"Q{o}){d}÷{e}: "))
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
            aq= (d, e) if d <= e else (e, d)
            if aq not in q:
                q.add(aq)
                break
             
        d3 = float(input(f"Q{p}){d}÷{e}: "))      
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