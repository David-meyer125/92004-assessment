#=========================================================================================================================================
#This function asks how many questions they want until they enter a number that is greater or equal to 15/just press enter
def how_many_questions():
  question_amount = 0
  while True:
    try:
      questions = input('How many questions would you like to answer (minimum 15) or (press enter for ∞infinite∞ mode!): ')
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
    print('∞Infinite mode!∞ (To exit infinite mode press "enter")')
  return question_amount, questions
#==========================================================================================================================================
how_many_questions()
