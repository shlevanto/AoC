import sys


def parse_input(file_name):
    with open(file_name, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    tiles = []
    for line in lines:
        a, b = line.split(",")
        tiles.append((int(a), int(b)))

    return tiles


def find_area(tile_1, tile_2):
    h = abs(tile_2[0] - tile_1[0]) + 1
    l = abs(tile_2[1] - tile_1[1]) + 1
    # print(f"area of {tile_1} and {tile_2} is {h * l}")

    return h * l


def solution_1(tiles):
    areas = []
    # iterate through tile list
    # for each tile find all tiles that are down and right
    # calculate areas
    for i, tile in enumerate(tiles):
        for another_tile in tiles:
            if tile[1] <= another_tile[1]:
                areas.append(find_area(tile, another_tile))

    # find max
    return max(areas)


def main():
    file_name = sys.argv[1]

    tiles = parse_input(file_name)
    result_1 = solution_1(tiles)

    print(f"Result 1: {result_1}")


if __name__ == "__main__":
    main()
