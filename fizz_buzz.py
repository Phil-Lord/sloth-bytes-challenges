def fizz_buzz(n):
    fuzz = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fuzz.append('FizzBuzz')
        elif i % 3 == 0:
            fuzz.append('Fizz')
        elif i % 5 == 0:
            fuzz.append('Buzz')
        else:
            fuzz.append(i)
    return fuzz

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
