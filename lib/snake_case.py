def convert(string):
    n = len(string)
    string = list(string)
    for i in range(n):
        if (string[i] == ' '):
            string[i] = '_'
        else:
            string[i] = string[i].lower()
    string = "".join(string)
    return string
