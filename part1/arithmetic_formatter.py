def arithmetic_arranger(problems, show_answers=False):
    #declaring strings for each row so that it takes only one iteration to generate the whole string
    final_string = ''
    first_row = ''
    second_row = ''
    third_row = ''
    fourth_row = ''
    
    #making list of all the operands and operators 
    first_operands = [problem.split(' ')[0] for problem in problems]
    second_operands = [problem.split(' ')[2] for problem in problems]
    operators = [problem.split(' ')[1] for problem in problems]
    
    #making a list of the max no of digits among operands for every operation
    max_length = [max(len(first_operands[i]), len(second_operands[i])) for i in range(len(problems))]
    
    if len(problems) > 5:       #if there are more than 5 problems, we generate an error
        return 'Error: Too many problems.'
    if not all(operator in ['+', '-'] for operator in operators):       #if there are any operators other than + or -, we generate an error
        return "Error: Operator must be '+' or '-'."
    if not (all(operand.isdigit() for operand in first_operands) and    
            all(operand.isdigit() for operand in second_operands)):         #if any operand contains characters that are not digits, we generate an error
        return 'Error: Numbers must only contain digits.'
    if any(len(operand) > 4 for operand in first_operands + second_operands):           #if any operand has more than 4 digits we generate an error
        return "Error: Numbers cannot be more than four digits."
    
    answers = []
    for i in range(len(problems)):          #iterating through every problem
        width = max_length[i] + 2           #width of the problem (width of the max operand + 2 spaces for ' +' or ' -' character)
        
        first_row += f"{first_operands[i].rjust(width)}    "
        second_row += f"{operators[i]} {second_operands[i].rjust(width - 2)}    "           #making the strings for 1st and 2nd row, adding 4 spaces after each problem (right justifying them too)
        third_row += '-' * width + '    '
        
        if show_answers:            #calculating answers if answers required and appending it to the answers list
            if operators[i] == '+':
                result = int(first_operands[i]) + int(second_operands[i])
            elif operators[i] == '-':
                result = int(first_operands[i]) - int(second_operands[i])
            answers.append(str(result).rjust(width))  
    final_string = first_row.rstrip() + '\n' + second_row.rstrip() + '\n' + third_row.rstrip()      #combining all the strings to make a final string. using strip function because of the 4 spaces at the end of each string
    if show_answers:
        fourth_row = '    '.join(answers)
        final_string += '\n' + fourth_row
    
    return final_string

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
