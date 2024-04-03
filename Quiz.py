questions = [
         
           "Q1] WHAT IS THE CAPITAL CITY OF INDIA ?",
           "Q2] WHAT IS THE CAPITAL CITY OF JAPAN ?",
           "Q3] WHAT IS THA CAPITAL CITY OF JHARKHAND  ?",
           "Q4] WHAT IS THE CAPITAL CITY OF PAKISTAN  ?",
           "Q5] WHAT IS THE CAPITAL CITY OF LADDAKH ?",
           "Q6] WHAI IS THE CAPITAL CITY OF FRANCE ?"
             
            ]


options = [
    
          ("A. DELHI", "B. NOIDA", "C. GAZIABAD", "D. LAKHNOW"),
          ("A. BIZING", "B. TOKYO", "C. CHAINA", "D. AMERICA"),
          ("A. LAKHNOW", "B. DELHI", "C. GAZIPUR", "D. RACHI"),
          ("A. LAHORE", "B. LAEH", "C. ISLAMABAD", "D. PTHANCORT"),
          ("A. LEAH", "b. JAMMU", "C. SIRYA", "D. KASMIR"),
          ("A. LONDON","B. PARISH","C.AMERICA","D CANADA")
          
          ]
          
          
Answers = ("A","B","D","C","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("_____________________________")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == Answers[question_num]:
        score += 1
        print("_____________________________")
        print("CORRECT 😎")
    else:
        print("INCORRECT 😞") 
        print(f"{Answers[question_num]} is tha correct Answer")
    
    question_num +=1   
    
    
print("----------------")    
print("----------------")
print("    RESULT      ")
print("----------------")
print("----------------")

        
        
        
print("Answers: ", end=" ")       
for Answer in Answers:
    print(Answer ,end=" ")
print()   

print("guesses: ", end=" ")
for guess in guesses:
    print(guess,end=" ")
print()    

score = int(score/len(questions) *100)
print(f"your score is : {score}% ")