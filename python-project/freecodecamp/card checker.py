def verify_card(card_number):
    reverse_card = card_number[::-1]

    sum_of_odd_digits = 0
    odd_digits = reverse_card[::2]  # typically every other digit starting at index 0
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = reverse_card[1::2]
    for digit in even_digits:
        number = int(digit) * 2  # usually, you need to double every even-position digit
        if number > 9:  # if doubling makes it two digits
            number -= 9  # same as adding the two digits together
        sum_of_even_digits += number

    total = sum_of_even_digits + sum_of_odd_digits
    return total % 10 == 0

def get_card():
    card_numbers = input('Please enter your card number (xxxx-xxxx-xxxx-xxxx): ')
    
    # Check if the input follows the required format
    if not re.fullmatch(r'\d{4}-\d{4}-\d{4}-\d{4}', card_numbers):
        print('Invalid format, ensure card follows xxxx-xxxx-xxxx-xxxx.')
        return  # Exit the function if format is wrong

    # Remove dashes (and spaces if any)
    card_reader = str.maketrans({'-': '', ' ': ''})
    card_reader_numbers = card_numbers.translate(card_reader)
    
    # Verify the card using the Luhn algorithm
    if verify_card(card_reader_numbers):
        print('Valid card number')
    else:
        print('Invalid card number')

get_card()




        
        