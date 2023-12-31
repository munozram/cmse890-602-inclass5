def reverse_string(mystring  ):
    """
    Reverses the ordering of characters in a string using a simple loop.
    Input: a string.
    Output: a completely reversed version of that string, including all characters.
    """

    reversed_string = ""

    if len(mystring) == 0:
        return []

    for i in range(len(mystring) - 1, -1, -1):
        reversed_string += mystring[i]

    return reversed_string


mystring = "Go green!"

print("\noriginal string:    ", mystring, "\n")
reversed = reverse_string(mystring)


print("reversed string:    ", reversed, "\n")
