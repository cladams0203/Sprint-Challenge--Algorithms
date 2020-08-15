'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    search_string = 'th'
    search_string_length = len(search_string)
    if len(word) < search_string_length:
        return 0
    if word[0:search_string_length] == search_string:
        return count_th(word[search_string_length - 1:]) + 1
    return count_th(word[search_string_length - 1:])