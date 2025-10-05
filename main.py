def format_string(string, length):
    if len(string) >= length:
        return string
    spaces = (length - len(string)) // 2
    return (' ' * spaces + string)