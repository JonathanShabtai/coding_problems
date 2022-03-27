def replace_spaces(input_string, s):
    answer = ''
    i = 0
    while i < s:
        if input_string[i] == ' ':
            answer += '%20'
        else:
            answer += input_string[i]
        i += 1

    return answer

def replace_space_one_liner(input_string, s):
    return '%20'.join(input_string[:s].split())


print(replace_spaces('Mr John Smith   ', 13))
print(replace_space_one_liner('Mr John Smith   ', 13))
