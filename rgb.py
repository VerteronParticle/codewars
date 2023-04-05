"""Convert RGB to six-digit Hexadecimal."""
def rgb(r, g, b):
    """Validate and return six-digit Hexadecimal."""""
    def valid(num):

        return 255 if num > 255 else (
            0 if num < 0 else num
        )

    def valid_hex(num):

        return hex(num)[2:] if num > 10 else (
            f"0{hex(num)[2:]}" if num < 10 else "00"
        )
    output = list(map(valid_hex, map(valid, [r, g, b])))
    return ''.join([n for n in output]).upper()
