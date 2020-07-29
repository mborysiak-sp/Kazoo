def set_token():
    f = open("../token.txt", "r")
    if f.mode == 'r':
        return f.read()
    else:
        raise Exception("Wrong file object mode")
