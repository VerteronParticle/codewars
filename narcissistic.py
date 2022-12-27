def narcissistic(value):
    import math
    return (
        sum([(int(i) ** (int(math.log10(value) + 1))) for i in str(value)])
    ) == value


print(narcissistic(153))
