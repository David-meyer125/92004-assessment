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
instructions()
#=========================================================================================================================================