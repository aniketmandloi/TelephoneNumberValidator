import re
def telephoneCheck(string):
    # First check to make sure that the first character is either a digit
    # or an opening parenthesis. This will disallow "-1 (757) 622-7382"
    first_char_check = string[0].isdecimal() or string[0] == "("
    # Extract just the digits from the string
    tele_digits = [int(char) for char in string if char.isdecimal()]
    num_digits = len(tele_digits)
    # Check if the length is 10 or 11
    # If the length is 11, check that the country code is 1
    length_check = num_digits == 10 or (num_digits == 11 and tele_digits[0] == 1)
    # Create a regular expression to check for the pattern "(XXX)"
    # Where X is any character
    parens_regex = r"\(.{3}\)"
    # Check to see if the string contains any parentheses
    # If it does, make sure that it matches the parentheses regex exactly once
    parens_check = True
    if ("(" in string) or (")" in string):
        parens_match = re.findall(parens_regex, string)
        #print(parens_match)
        parens_check = (parens_match is not None) and (len(parens_match) == 1)
    return first_char_check and length_check and parens_check
