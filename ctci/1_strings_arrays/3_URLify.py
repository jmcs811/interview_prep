# problem: Wreite a method to replace all spcaes in a string with '%20'. You may assume
#          that the string has sufficient space at the end to hold the additional characters
#          and you are given the true lenght of the string

# Example:
#   INPUT: "Mr John Smith", 13
#   OUTPUT: "Mr%20John%20Smith"

def urlify(item):
    '''
    TIME:
    SPACE:
    '''
    # count the spaces
    result = ""
    for i in item:
        if i == ' ': 
            result = f'{result}%20'
        else:
            result = f'{result}{i}'
    return result
