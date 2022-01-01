def arithmetic_arranger(problems, results=False):
    
    # Raise error if problems' length is greater than 5
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Split problems on space; obatin 3 strings per problem.
    lines = ['', '', '']
        
    problems_split = []
    for i, el in enumerate(problems):
        problems_split.append([])
        problems_split[i] = el.split()
    
    # Check if conditions are met
    for problem in problems_split:
        # Raise error if numbers are longer than 4 digits
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        # Raise error if operators are not '+' or '-'
        if problem[1] not in '+-':
            return "Error: Operator must be '+' or '-'."
        # Raise error if operands contain other than digits.
        if not problem[0].isnumeric() or not problem[2].isnumeric():
            return 'Error: Numbers must only contain digits.'
        
    # Calculate operations results if results is True    
    if results:
        lines.append('')
        for problem in problems_split:
            if problem[1] == '+':
                problem.append(str(int(problem[0]) + int(problem[2])))
            else:
                problem.append(str(int(problem[0]) - int(problem[2])))
    
    for problem in problems_split:
        # Store sign, operands and their length in variables to improve readability
        operand_1 = problem[0]
        operand_2 = problem[2]
        sign = problem[1]
        operand_1_len = len(operand_1)
        operand_2_len = len(operand_2)
        # Store total if we are calculating them:
        total = ''
        if results:
            total = str(problem[3])
        
        # How to proceed if operand_1 is greater than or equal to operand_2
        if operand_1_len >= operand_2_len:
            # Add two leading spaces to operand_1 to account for
            # op_2 sign and space
            operand_1 = ' '*2 + operand_1
            # Update operand_1 length
            operand_1_len = len(operand_1)
            # Add sign length to operand_2
            operand_2_len = len(operand_2) + 1
            # Add leading spaces to operand_2
            operand_2 = sign + ' '*(operand_1_len - operand_2_len) + operand_2
            # Update operand_2 length
            operand_2_len = len(operand_2)
        # How to proceed if operand_2 is greater than operand_1
        elif operand_2_len > operand_1_len:
            # Calculate and add leading spaces to op_1
            operand_1 = ' '*(operand_2_len - operand_1_len + 2) + operand_1
            # Update op_1 length
            operand_1_len = len(operand_1)
            # Add sign and space at front of op_2
            operand_2 = sign + ' ' + operand_2
            # Update op_2 length
            operand_2_len = len(operand_2)
        
        # --Generate list 'lines' content--    
        # Add first operand and trailing space
        lines[0] += operand_1 + ' '*4
        # Add sign, second operand and trailing space
        lines[1] += operand_2 + ' '*4
        # Add slashes
        lines[2] += '-'*operand_1_len + ' '*4
        # Add results if True
        if results:
            lines[3] += ' '*(operand_2_len-len(problem[3])) + problem[3] + ' '*4
        
    arranged_problems = """"""
    
    for line in lines:
        if line == lines[-1]:
            arranged_problems += line.rstrip()
        else:
            arranged_problems += line.rstrip() + '\n'
    
    return arranged_problems