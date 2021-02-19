import typing as t

def unit_box(plot: t.Tuple[int, int]) -> t.Tuple[int, int]:
    x, y = plot
    if x % y == 0:
        return (y, y)
    elif y % x == 0:
        return (x, x)
    new_plot = (min(x, y), max(x, y) % min(x, y))
    return unit_box(new_plot)


if __name__ == "__main__":
    cases = [
    (1680, 640),
    (1000,1000),
    (19524123, 5949),
    ]

    for case in cases:
        print(unit_box(case))