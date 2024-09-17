def arithmetic_arranger(problems, show_answers=False):
    final_string = ''
    first_row = ''
    second_row = ''
    third_row = ''
    fourth_row = ''
    
    first_operands = [problem.split(' ')[0] for problem in problems]
    second_operands = [problem.split(' ')[2] for problem in problems]
    operators = [problem.split(' ')[1] for problem in problems]
    
    max_length = [max(len(first_operands[i]), len(second_operands[i])) for i in range(len(problems))]
    
    if len(problems) > 5:
        return 'Error: Too many problems.'
    if not all(operator in ['+', '-'] for operator in operators):
        return "Error: Operator must be '+' or '-'."
    if not (all(operand.isdigit() for operand in first_operands) and 
            all(operand.isdigit() for operand in second_operands)):
        return 'Error: Numbers must only contain digits.'
    if any(len(operand) > 4 for operand in first_operands + second_operands):
        return "Error: Numbers cannot be more than four digits."
    
    answers = []
    for i in range(len(problems)):
        width = max_length[i] + 2
        
        first_row += f"{first_operands[i].rjust(width)}    "
        second_row += f"{operators[i]} {second_operands[i].rjust(width - 2)}    "
        third_row += '-' * width + '    '
        
        if show_answers:
            if operators[i] == '+':
                result = int(first_operands[i]) + int(second_operands[i])
            elif operators[i] == '-':
                result = int(first_operands[i]) - int(second_operands[i])
            answers.append(str(result).rjust(width))  
    final_string = first_row.rstrip() + '\n' + second_row.rstrip() + '\n' + third_row.rstrip()
    if show_answers:
        fourth_row = '    '.join(answers)
        final_string += '\n' + fourth_row
    
    return final_string

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
