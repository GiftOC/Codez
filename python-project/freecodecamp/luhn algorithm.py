def verify_card_number(card_number):
      card_number_reversed = card_number[::-1]
      
      sum_of_odd_digits = 0
      odd_digits = card_number_reversed[:: 2]
      for digit in odd_digits:
            sum_of_odd_digits += (int(digit))
      
      
      sum_of_even_digits = 0
      even_digit = card_number_reversed[1:: 2]
      for digit in even_digit:
            number = int(digit) * 2
            if number >= 10:
                  number = number // 10 + number % 10
            sum_of_even_digits += number

      total = sum_of_odd_digits + sum_of_even_digits 
      return 0 == total % 10     



def main():
      card_number = '4105-4100-2395-0807'
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card = card_number.translate(card_translation)
      if verify_card_number(translated_card) is True:
            print('valid')
      else:
            print('invalid')
main()