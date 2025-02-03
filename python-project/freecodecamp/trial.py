def verify_cc(cc_number):

      reversed_number = cc_number[::-1]

      sum_single_numbers = 0
      single_number = reversed_number[::2]
      for digits in single_number:
            sum_single_numbers += int(digits)

      sum_double_numbers = 0
      double_number = reversed_number[1::2]
      for digits in double_number:
            number = int(digits)
            if number > 9:
                  number -= 9
            sum_double_numbers += number

      total = sum_double_numbers + sum_single_numbers
      return total % 10 == 0

import re
def cc_details():
      cc_number = input("Enter your card number (xxxx-xxxx-xxxx-xxxx): ")

      if not re.fullmatch(r'\d{4}-\d{4}-\d{4}\d{4}', cc_number):
            print('invlid input, ensure card follows xxxx-xxxx-xxxx-xxxx')
            return
      card_reader = str.maketrans({'-': '', ' ': ''})
      card_number = cc_number.translate(card_reader)

      if verify_cc(card_number):
            print('valid')
      else:
            print('invalid')

