def is_polyndrome(teststr):
    comparing_result = False
    #lower case
    str_lower = teststr.lower()
    #remove punctuation
    str_alpha = ""
    for x in str_lower:
        if x.isalpha():
            str_alpha += x
    #reverse
    str_reversed = str_alpha[::-1]
    #compare strings
    if str_alpha == str_reversed:
        comparing_result = True
    return comparing_result

print(is_polyndrome("Madam, I'm Adam"))