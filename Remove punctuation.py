def func(s):
    t = ''
    for n in s:
        if n in ',.;:!?':
            continue
        else:
            t += n
    return t

print(func(input('Input a string: ')))
