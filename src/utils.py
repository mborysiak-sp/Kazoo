def get_token(token_name):
    f = open(f"../tokens/{token_name}", "r")
    if f.mode == 'r':
        return f.read()
    else:
        raise Exception("Wrong file object mode")
