def solution(number):
    r = 0
    for n in range(number - 1, -1, -1):
        if (n % 3 == 0 or n % 5 == 0):
            r += n
    return r if r > 0 else 0