import re


def parse_input(input_lines):
    coefficients = []
    constants = []
    for line in input_lines:
        split_line = line.split()
        var_map = {}
        for index in range(0, len(split_line)):
            is_negative = False
            if split_line[index - 1] == '-':
                is_negative = True
            find_var = re.search('[a-zA-Z]', split_line[index])
            if find_var is not None:
                find_coef = re.search("[+]?\d*\.?\d+|[+]?\d+", split_line[index])
                if find_coef is not None:
                    var_map[find_var.group()] = int(find_coef.group())
                else:
                    var_map[find_var.group()] = 1
                if is_negative:
                    var_map[find_var.group()] = -var_map.get(find_var.group())

        coefficients_line = []
        for variable in ['x', 'y', 'z']:
            if variable in var_map:
                v = var_map.get(variable)
                coefficients_line.append(v)
            else:
                coefficients_line.append(0)
        coefficients.append(coefficients_line)
        constants.append(int(split_line[-1]))
    return coefficients, constants

