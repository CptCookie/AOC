WIDTH = 25
HEIGHT = 6

BLACK = "0"
WHITE = "1"
TRANS = "2"


def parse_input(aoc_input: str) -> list[str]:
    aoc_input = aoc_input.replace("\n", "")
    return [
        aoc_input[start : start + WIDTH * HEIGHT]
        for start in range(0, len(aoc_input), WIDTH * HEIGHT)
    ]


def get_decode_pixel(image, pixel: int):
    for layer in image:
        if layer[pixel] != TRANS:
            return layer[pixel]
    return TRANS


def solution_1(aoc_input: str):
    image = parse_input(aoc_input)

    zero_cnt = [layer.count(BLACK) for layer in image]
    min_idx = zero_cnt.index(min(zero_cnt))

    return image[min_idx].count(WHITE) * image[min_idx].count(TRANS)


def solution_2(aoc_input: str):
    image = parse_input(aoc_input)

    decoded_image = [get_decode_pixel(image, pixel) for pixel in range(HEIGHT * WIDTH)]
    print()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if decoded_image[WIDTH * y + x] == BLACK:
                print("\u2007", end="")
            else:
                print("\u2588", end="")
        print()
    return "Read solution above!"
