def capital_case(s):
    if not isinstance(s, str):
        raise TypeError('Please provide a string argument')
    return s.capitalize()
