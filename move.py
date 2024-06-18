def move(s):
    s_moved = ''
    for c in list(s):
        s_moved += chr(ord(c) + 1)
    print(s_moved)

move('hello')
move('bye')
move('welcome')