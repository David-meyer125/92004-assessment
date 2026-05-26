import random
acceptable_yes_response = ['Yes','Y','Yep','Sure','Ok','Yea','Yup','Definitely','Absolutely'] 
acceptable_no_response = ['No','N','Nah','Nope',] 
#==========================================================================================================================================
#This function shows the starting message and asks if they want the instructions and keeps asking until they enter yes or no
def instructions():
  print('')
  print('====Welcome to the Basic Facts Math Quiz!====')
  print('')
  while True:
    yes_no = input('í ½í·ŽWould you like to see the instructions?í ½í·Ž ').strip().title()
    if yes_no in acceptable_yes_response:
      print('í ½í·ŽHere are the instructionsí ½í·Ž')
      print('')
      print('This quiz will be based around basic facts') 
      print('When answering questions you must enter a number to be able to move on to the next question.') 
      print('If you choose division answers will be rounded to 2 decimal places')
      print('Most importantly good Luck and Have Fun!')
      break
    elif yes_no in acceptable_no_response:
      break
    else:
      print('')
      print('Please enter "Yes" or "No"')

#=========================================================================================================================================
#This function asks how many questions they want until they enter a number that is greater or equal to 15/just press enter
def how_many_questions():
  question_amount = 0
  while True:
    try:
      questions = input('How many questions would you like to answer (minimum 15) or (press enter for âˆžinfiniteâˆž mode!): ')
      questions = int(questions)
      if questions >= 15:
        question_amount = questions
        break
      elif questions < 15:
        print('')
        print('Please enter an number/integer that is 15 or over')
    except ValueError:
      if questions == '':
        break
      else:
        print('')
        print('Please enter a valid integer/number')
  if question_amount == 0:
    print('âˆžInfinite mode!âˆž (To exit infinite mode press "enter")')
  return question_amount, questions
#==========================================================================================================================================
#This function generates a random number based on the range they chose earlier and finds the answer using the equation based on what symbol the chose
def question_generator(what_is_symbol, smallest, biggest):
  number_1 = random.randint(smallest,biggest)
  number_2 = random.randint(smallest,biggest)
  if what_is_symbol == '+' :
    answer = number_1 + number_2
  elif what_is_symbol == '-' :
    answer = number_1 - number_2
  elif what_is_symbol == '*' :
    answer = number_1 * number_2
  elif what_is_symbol == '/' :
    while True:
      answer = number_1 / number_2
      answer = round(answer, 2)
      if number_1 < number_2:
        answer = number_2 / number_1
        answer = round(answer,2)
        what_was_question = (f'What is {number_2} {what_is_symbol} {number_1}? ')
        break
      else:
        what_was_question = (f'What is {number_1} {what_is_symbol} {number_2}? ')
        break
  if what_is_symbol != '/':
    what_was_question = (f'What is {number_1} {what_is_symbol} {number_2}? ')
  return answer, what_was_question
#========================================================================================================================================== 
#This is the main quiz loop it runs whether they choose infinite mode or limited mode and only finishes if they reach the amount of questions they chose (limited) or
# until the user presses enter (infinite mode)
def the_quiz(question_amount,symbol_type, smallest_number, largest_number):
  what_question = [] 
  user_answers = []
  correct_answer = []
  question_correct = 0 
  question_incorrect = 0 
  question_answered = 0 
  print(f'====================Question {question_answered + 1}====================')
  while question_answered < question_amount or question_amount == 0:
    answer, what_was_question = question_generator(symbol_type, smallest_number, largest_number)
    while True:
      answer_the_question = input(what_was_question)
      if question_amount == 0 and answer_the_question == '':
        return what_question, user_answers, question_correct, question_incorrect, question_answered, correct_answer
      try:
        answer_the_question = float(answer_the_question)
        break
      except ValueError:
        print('Please enter a valid integer/number')
#Here I check if the answer was right or wrong then appended their history to a list and increase some variables to later print out        
    if answer_the_question == answer:
      print('Correct!')
      question_correct = question_correct + 1                       
    else:
      print('Incorrect')
      print(f'The answer is {answer}')
      question_incorrect = question_incorrect + 1
    question_answered = question_answered + 1
    if symbol_type == "/":
      user_answers.append(answer_the_question)
    else:
      answer_the_question = int(answer_the_question)
      user_answers.append(answer_the_question)
    correct_answer.append(answer)
    what_question.append(what_was_question)
    if question_answered < question_amount or question_amount == 0:
      print(f'====================Question {question_answered + 1}====================')
  return what_question, user_answers, question_correct, question_incorrect, question_answered, correct_answer     
  
#==========================================================================================================================================

#This function prints out the questions they answered if they want aswell as the percentage they got right
def results_seq(what_question, user_answers, correct_answer, question_correct, question_answered):
  number_of_question = 0
  question_number = 0
  comment = "nothing"
  while True:
    results = input('Would you like to see your results? ').strip().title()  
    if results in acceptable_yes_response:
      if len(user_answers) >= 1:
        for i in range(len(what_question)):
          print('===================================================================================')
          print(f'Question {i+1} was {what_question[i]}')
          print('')
          print(f'For question {i+1} you got {user_answers[i]} and the answer was {correct_answer[i]}')
          print('===================================================================================')
        break
      else:
        break
        
    elif results in acceptable_no_response:
      break
    else:
      print('')
      print('Please enter "Yes" or "No"')
  
  if len(user_answers) >= 1:  
    questions_right_percentage = question_correct / question_answered * 100 
    questions_right_percentage = round(questions_right_percentage)
    #Here based on how much percent they got I give them a little comment on how they did
    if questions_right_percentage >= 80:
      comment = "excellent work"
    elif questions_right_percentage >= 60:
      comment = "Wow amazing"
    elif questions_right_percentage >= 40:
      comment = "Nice job"
    elif questions_right_percentage >= 20:
      comment = "good work you're getting there"
    elif questions_right_percentage >= 0:
      comment = "You need more practice"
    print(f'í ¼í¾‰You got {questions_right_percentage}% correct {comment}!í ¼í¾‰')
    print('')
  else:
    print('You did not answer any questions')
  print('Thank you for doing my quiz!')
#==========================================================================================================================================
#This function checks if what they input was in the list I made and if it is assigns the symbol_type variable a symbol
possible_symbols = { '1': '+', '2': '-', '3': '*', '4': '/' }
def what_symbol():
  print('What symbol would you like your questions to use?')
  print('Easy modes!')
  print('1. + Addition')
  print('2. - Subtraction')
  print('')
  print('Advandced modes!')
  print('3. * Multiplication')
  print('')
  print('Impossible mode! (warning questions are very difficult)')
  print('4. / Division (answers will be rounded to 2 d.p)')
  symbol = input('Please enter 1, 2, 3, or 4 : ').strip().title()
  symbol_type = 'nothing'
  while True:
    if symbol in possible_symbols:
      symbol_type = possible_symbols[symbol]
      break
    else:
      print('')
      symbol = input("Please enter only 1, 2, 3, or 4 : ").strip().title()

  print(f' You chose {symbol_type}')
  return symbol_type

#==========================================================================================================================================
#This function checks if what they input was in the list I made and if it is assigns the smallest_number and largest_number variables a number each to get the range
difficulty_options = { "1": (1, 100), "2": (51, 200), "3": (201, 400), "4": (1, 999) }
def how_difficult():
  print('What range of numbers would you like your questions to have?')
  print('1. 1 -> 100')
  print('2. 51 -> 200')
  print('3. 201 -> 400')
  print('4. 1 -> 999')
  difficulty = input('Please enter 1, 2, 3, or 4 : ').strip().title()
  smallest_number = 0
  largest_number = 0
  while True:
    if difficulty in difficulty_options:
      smallest_number, largest_number = difficulty_options[difficulty]
      break
    else:
      print('')
      difficulty = input("Please enter only 1, 2, 3, or 4 : ").strip().title()
  return smallest_number, largest_number
#==========================================================================================================================================
#Here all the functions are put into a while true loop and runs the quiz automatically when the code is first run then once everything is done
#asks if they would like to play again and if they say yes it runs again otherwise it stops the code
#Actual code below

play_again = 'Yes'
while True:
  if play_again in acceptable_yes_response:
    instructions()
    print('')
    symbol_type = what_symbol()
    print('')
    smallest_number, largest_number = how_difficult()
    print('')
    question_amount, questions = how_many_questions()
    print('')
    what_question, user_answers, question_correct, question_incorrect, question_answered, correct_answer, = the_quiz(question_amount, symbol_type, smallest_number, largest_number)
    print('')
    results_seq(what_question, user_answers, correct_answer, question_correct, question_answered)  
    play_again = input('Would you like to play again? ').strip().title()
    
  elif play_again in acceptable_no_response:
      break
    
  else:
    while play_again not in acceptable_no_response and play_again not in acceptable_yes_response:
      play_again = input('Please enter "yes" or "no" ').strip().title()
      
    
#==========================================================================================================================================