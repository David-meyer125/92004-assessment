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