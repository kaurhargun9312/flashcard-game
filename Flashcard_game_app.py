user = input("Hi, Give a username for you: ")
print("PERFECT! " , user, " Lets start the quiz, BEST OF LUCK!! ")
Flashcards = {
    "What color is the sky on a clear day?": "Blue",
    "How many legs does a spider have?": "8",
    "What is 5 + 3?": "8",
    "What fruit is known for keeping the doctor away if you eat one a day?": "Apple",
    "What do bees make?": "Honey",
    "Which planet do we live on?": "Earth",
    "What sound does a cow make?": "Moo",
    "How many days are in a week?": "7",
    "What is the opposite of hot?": "Cold",
    "What do you use to write on a blackboard?": "Chalk"
 }
Flashcards_med = {
  "What is the main part of a computer called?": "CPU",
  "What is 2 + 2 in Python?": "4",
  "What symbol is used for multiplication in Python?":	"*",
  "Which keyword is used to make a loop in Python?": "for",
  "What do we use to show output in Python?" : "print",
  "What is the file extension for Python files?":	".py",
  "Which device lets you type into a computer?": "Keyboard",
  "What is the name of the computers brain?": 	"CPU",
  "Which Python keyword starts a function?":	"def",
  "What does HTML stand for? (a bit techy but simple)": "HyperText Markup Language",
 }

Flashcards_hard = {
  "What is the output of: 3 * (2 + 5) - 4 ** 2 in Python?": "1",
  "How many bits are in 2 bytes?": "16",
  "What is the value of binary 1010 + 0101? (in decimal)": "15",
  "Which built-in Python function returns the absolute value of a number?": "abs",
  "What does '//' do in Python when used between two numbers?": "Floor division",
  "Evaluate: round(13.67) + int(4.9) = ?": "18",
  "What is the hexadecimal value of 255?": "FF",
  "What is the result of 2 ** 3 ** 1 in Python?": "8",
  "Which math module function returns the square root of a number?": "sqrt",
  "What does 7 % 3 return in Python?": "1"
}

while True:
 print("1. Easy \n 2. Medium \n 3. Hard \n 4. Exit")
 choice = input("Choose what level you want to play? ")
 choice = int(choice)
 if choice == 1:
  Score = 0
  for Question,answer in Flashcards.items():
    user_answer = input( Question + " " )
    if user_answer.lower() == answer.lower():
        print("Correct you got it right :) ")
        Score += 1
    else:
        print("Oops wrong one!! ")
  print("Your Final Score is: " + str(Score) + " points")
 elif choice == 2:
    Score_med = 0
    for question, answer in Flashcards_med.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct! You got it right :)")
            Score_med += 1
        else:
            print("Oops, wrong one!!")
    print("Your Final Score is: " + str(Score_med) + " points")

 elif choice == 3:
      Score_hard = 0
      for Question,answer in Flashcards_hard.items():
          user_answer = input( Question + " " )
          if user_answer.lower() == answer.lower():
             print("Correct you got it right :) ")
             Score_hard += 1
          else:
            print("Oops wrong one!! ")
      print("Your Final Score is: " + str(Score_hard) + " points")
 elif choice == 4:
   print("Thankyou! have a great day :) ")
   break
 else:  
   print("you selected a wrong option")







