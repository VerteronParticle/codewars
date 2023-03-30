"""Create phone number."""


def create_phone_number(num):
    """Create a phone number from a list of 10 numbers."""
    return f"""({''.join(
        str(n) for n in num[:3]
    )}) {''.join(
        str(n2) for n2 in num[3:6]
    )}-{''.join(
        str(n2) for n2 in num[6:10]
    )}"""


if __name__ == "__main__":
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
