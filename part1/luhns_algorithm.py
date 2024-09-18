'''This program impliments the Luhn's algo to check whether a given creditcard is valid or not. The Luhn's algo is described as follows:
We start from the rightmost digit and move leftm while doubling every second digit from the right. If doubling the number results in a 
number greater than 9, we subtract 9 from the result. We then sum all the digits together, including both the unchanged and the processed 
digits. If the total is divisible by 10, the number is valid. If it's not divisible by 10, the number is invalid.'''


def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '3379-5135-6110-8795'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()