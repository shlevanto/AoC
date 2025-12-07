import sys
from socket import IPPORT_RESERVED


def parse_input(file_name):
    with open(file_name, "r") as f:
        input_string = [line.strip() for line in f.readlines()]

    input_string[0] = input_string[0].replace("S", "|")

    layers = [list(s) for s in input_string]

    return layers


def solution_1(layers):
    beam_splits = 0

    beam_initiation = layers[0]

    for layer in layers[1:]:
        beam_indices = [i for i, b in enumerate(beam_initiation) if b == "|"]

        for i in range(len(layer)):
            if i in beam_indices:
                if layer[i] == "^":
                    beam_splits += 1
                    try:
                        layer[i - 1] = "|"
                    except:
                        pass
                    try:
                        layer[i + 1] = "|"
                    except:
                        pass
                else:
                    layer[i] = "|"
            beam_initiation = layer
    return beam_splits


def main():
    file_name = sys.argv[1]

    manifold = parse_input(file_name)
    result_1 = solution_1(manifold)

    print(f"Result 1: {result_1}")


if __name__ == "__main__":
    main()
