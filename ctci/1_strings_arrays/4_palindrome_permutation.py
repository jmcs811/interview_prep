# problem: Given a string write a function to check if it is a permuation of a palidrome.
#          A palidrome is a word or phrase that is the same forwards and backwords. 
#          A permuation is a rearrangement of letters. The palidrome does not need to be 
#          limited to just dictonary words.

# I/O: Input is a string, Output is a boolean value

# inital idea
# create a hash table
# loop through the string
# count the number of times a char appears
# if there is only 1 odd number char it is true
def palidrome_permutation(item):
    ht = {}
    for i in item:
        if i == ' ':
            continue
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    # loop through to see if there is more than 1 odd char
    oddFound = 0
    for key, val in ht.items():
        if val % 2 == 1:
            oddFound += 1

    print(ht)
    print(oddFound)
    return oddFound <= 1

print(palidrome_permutation('tact coa'))
        