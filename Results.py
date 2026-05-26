acceptable_yes_response = ['Yes','Y','Yep','Sure','Ok','Yea','Yup','Definitely','Absolutely'] 
acceptable_no_response = ['No','N','Nah','Nope',] 
#Change these as pleased
what_question = ['Test variable value', 'Test variable value', 'Test variable value']
user_answers = ['Test variable value', 'Test variable value', 'Test variable value']
correct_answer = ['Test variable value', 'Test variable value', 'Test variable value']
question_correct = 3
question_answered = 3
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
results_seq(what_question, user_answers, correct_answer, question_correct, question_answered)