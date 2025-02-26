#saved as Quiz_Game.py

print("Hello!, Welcome to our Quiz Game")

play=input("Do you want to play game? ")

if play.lower() == "yes":
    
   print(" Now you can countinue our game.")
   print(" Write the output of the following equations.")

   score = 0

   print("Question 1: 84/6*5+7-9")
   q1=input("Answer: ")


    
   if q1 =="88":
        print("Your answer is correct")
        score+=1
   else:
        print("Answer is Wrong")
            


   print("Quection 2: 5*5+4(5*3)")
   q2=input("Answer: ")
        
   if q2=="85":
        print("Answer is correct")
        score+=1
   else:
        print("Answer is wrong")


   print("Quection 3: 12-12/4%2**2//6")
   q3=input("Answer: ")
        
   if q3=="12.0":
        print("Answer is correct")
        score+=1
   else:
        print("Answer is wrong")


        
   print("Quection 4: 8%5+7*2//6")
   q4=input("Answer: ")
        
   if q4=="5":
        print("Answer is correct")
        score+=1
   else:
        print("Answer is wrong")

        

   print("Quection 5: 68+4(5*3)-58%4*5//7")
   q5=input("Answer: ")
        
   if q5=="202":
        print("Answer is correct")
        score+=1
   else:
        print("Answer is wrong")

   print("your score is", score)
   print("your score is" +" " + str(((score/5))*100) + "%.")

else:
    print("OK, Try another time")

    

    

    

