import random
#Change these variables to test
smallest_number = 1
largest_number = 999
symbol_type = '+'
#change to 0 for infinite mode
question_amount = 15
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

the_quiz(question_amount,symbol_type, smallest_number, largest_number)