# -*- coding: utf-8 -*-

def luhn_algorithm(card_number):
    """
    Credit card numbers are validated by an algorithm called `Luhn's Algorithm`
    
    1. Double the value of every second digit.
    2. If the result of this doubling operation is greater than 9 (e.g 16), then add the digits of the product (e.g 1 + 6 = 7).
    3. Take sum of all the digits.
    4. If the total ends in zero, this is a valid card number, if not, it is an invalid card number.
    """
    
    # Reverse the card number and convert it to a list of integers
    card_number = [int(x) for x in str(card_number)]

    # Double every second digit from the right (odd positions, from 1-based indexing)
    for i in range(-2, -len(card_number)-1, -2):
        card_number[i] = card_number[i] * 2
        # If doubling results in a number greater than 9, subtract 9

        if card_number[i] > 9:
            card_number[i] -= 9
    print('card_number:', card_number)

    # Calculate the sum of all digits
    total = sum(card_number)
    print('total:', total)

    # If the sum is divisible by 10, the number is valid
    return total % 10 == 0

    
# Example usage
c_num = "4532015112830366"
c_num = "4137894711755904"
c_num = "5199110303040163"


if luhn_algorithm(c_num):
    print("Valid credit card number.")
else:
    print("Invalid credit card number.")
