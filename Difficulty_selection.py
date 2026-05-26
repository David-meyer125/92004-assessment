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
how_difficult()
#==========================================================================================================================================