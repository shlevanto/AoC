import sys


def parse_input(file_name):
    with open(file_name, "r") as f:
        input_list = [line.strip() for line in f.readlines()]

    split_point = input_list.index("")

    id_ranges = [
        (int(value.split("-")[0]), int(value.split("-")[1]))
        for value in input_list[:split_point]
    ]

    product_list = [int(value) for value in input_list[split_point + 1 :]]

    return (id_ranges, product_list)


def check_id(product_id, id_ranges):
    for range in id_ranges:
        if range[0] <= product_id <= range[1]:
            return 1
    return 0


def solution_1(id_ranges, product_list):
    fresh = 0

    for product_id in product_list:
        fresh += check_id(product_id, id_ranges)

    return fresh


def combine_ranges(sorted_ranges, finished):
    # print(sorted_ranges)
    if finished:
        return sorted_ranges

    finished = True

    new_ranges = list()

    i = 0

    while i < len(sorted_ranges):
        if i == len(sorted_ranges) - 1:
            new_range = sorted_ranges[i]
        elif sorted_ranges[i][1] >= sorted_ranges[i + 1][0]:
            # print((sorted_ranges[i], sorted_ranges[i + 1]))
            new_range = (
                sorted_ranges[i][0],
                max(sorted_ranges[i][1], sorted_ranges[i + 1][1]),
            )
            finished = False
            # if a range is combined with the next one, we skip the next one
            i += 1
        else:
            new_range = sorted_ranges[i]

        new_ranges.append(new_range)
        i += 1

    return combine_ranges(new_ranges, finished)


def solution_2(id_ranges):
    id_ranges.sort()

    sorted_ranges = list()

    for i, r in enumerate(id_ranges):
        if i == len(id_ranges) - 1:
            new_range = r
        elif (
            r[0] <= id_ranges[i + 1][0] and r[1] >= id_ranges[i + 1][1]
        ):  # next range is within current range
            new_range = r
        else:
            new_range = (r[0], min(r[1], id_ranges[i + 1][0]))
        sorted_ranges.append(new_range)

    final_ranges = combine_ranges(sorted_ranges, False)
    # print(final_ranges)
    range_lengths = sum([b - a + 1 for (a, b) in final_ranges])

    return range_lengths


def main():
    file_name = sys.argv[1]

    id_ranges, product_list = parse_input(file_name)

    result_1 = solution_1(id_ranges, product_list)
    result_2 = solution_2(id_ranges)

    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")


if __name__ == "__main__":
    main()
