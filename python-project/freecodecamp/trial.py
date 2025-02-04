def verify_card(card_number):
    reversed_card = card_number[::-1]

    sum_of_oddindex = 0
    oddindex = reversed_card[::2]
    for digits in oddindex:
        sum_of_oddindex += int(digits)

      
    sum_of_evenindex = 0
    evenindex = reversed_card[1::2]
    for digits in evenindex:
        number = int(digits) * 2
        if number > 9:
            number -= 9
        sum_of_evenindex += number

    total = sum_of_evenindex + sum_of_oddindex
    return total % 10 == 0
 

def get_card():
    card_number = input('Enter card number(xxxx-xxxx-xxxx-xxxx): ')
    card_reading = str.maketrans({'-': '', ' ': ''})
    card_reader = card_number.translate(card_reading)
    print(card_reader)
    if verify_card(card_reader):
        print('Valid card number')
    else:
        print('Invalid card number')
get_card()
