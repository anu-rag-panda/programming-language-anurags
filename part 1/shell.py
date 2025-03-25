import basic

while True:
    text = input("anurags > ")
    tokens, error = basic.run('<stdin>', text, 'ftxt')
    
    if error:
        print(error.as_string())
    else:
        print(tokens)
