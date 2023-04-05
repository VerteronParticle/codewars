"""Build a tower of n_floors floors."""


def tower_builder(n_floors):
    """
    Build a tower n_floors tall.

    :param n_floors: integer representation
                     of total number of floors.
    :return export:  container of floor strings.
    """
    i = 1
    m = n_floors - 1
    export = []
    for d in range(n_floors):
        export.append(
            f"{(lambda x: ' ' * x)(m)}" +
            f"{(lambda x: '*' * (x + i))(d)}" +
            f"{(lambda x: ' ' * x)(m)}"
        )
        i += 1
        m -= 1
    return export
