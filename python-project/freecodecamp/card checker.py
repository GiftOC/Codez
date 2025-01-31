import re

def verify_card(card_number):
      reverse_card  = card_number[: : -1]

      sum_of_odd_digits = 0
      odd_digits = reverse_card[::1]
      for digits in odd_digits:
            sum_of_odd_digits += int(digits)

      sum_of_even_digits = 0
      even_digits = reverse_card[1::2]
      for digits in even_digits:
            number = int(digits)
            if number >= 10:
                  number = number // 10 + number % 10
            sum_of_even_digits += number

      total = sum_of_even_digits + sum_of_odd_digits
      return 0 == total % 10

def get_card():
      card_numbers = input('Please enter your card number (xxxx-xxxx-xxxx-xxxx): ')
      #if re.fullmatch(r'\d{4}-\d{4}-\d{4}-\d{4}', card_numbers):
      #      return card_numbers
      #else:
      #      print('invalid format, ensure card follows xxxx-xxxx-xxxx-xxxx.')
      #
      
      card_reader = str.maketrans({'-': '', ' ': ''})
      card_reader_numbers = card_numbers.translate(card_reader)
      if verify_card(card_reader_numbers) is True:
            print('valid card number')
      else:
            print('invalid card number')
get_card()



            