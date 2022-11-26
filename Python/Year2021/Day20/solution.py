import math


def parse_data(puzzle_input: str) -> list[str]:
    image_enhancer = [
        "1" if c == "#" else "0"
        for c in puzzle_input.split("\n\n")[0]
        if c not in [" ", "\n"]
    ]

    image = []
    for line in puzzle_input.split("\n\n")[1].splitlines():
        image.append(["1" if c == "#" else "0" for c in line])

    return image_enhancer, image


def iterate_image_window(image, fill):
    size = len(image)
    for y in range(-1, size + 1):
        for x in range(-1, size + 1):
            index_numbers = [(x + dx, y + dy) for dy in (-1, 0, 1) for dx in (-1, 0, 1)]
            yield "".join(
                [
                    image[_y][_x] if 0 <= _x < size and 0 <= _y < size else fill
                    for _x, _y in index_numbers
                ]
            )


def enhance_image(enhancer, image, fill):
    new_image = ""
    for i, window in enumerate(iterate_image_window(image, fill)):
        new_image += enhancer[int(window, 2)]
        if (i + 1) % (len(image) + 2) == 0:
            new_image += "\n"
    return [n for n in new_image.splitlines() if n != ""]


def solution_1(puzzle_input: str):
    enhancer, image = parse_data(puzzle_input)

    for n in range(2):
        fill = enhancer[-1] if n % 2 == 1 and enhancer[0] == "1" else enhancer[0]
        image = enhance_image(enhancer, image, fill)

    return "".join(image).count("1")


def solution_2(puzzle_input: str):
    enhancer, image = parse_data(puzzle_input)

    for n in range(50):
        fill = enhancer[-1] if n % 2 == 1 and enhancer[0] == "1" else enhancer[0]
        image = enhance_image(enhancer, image, fill)

    return "".join(image).count("1")
