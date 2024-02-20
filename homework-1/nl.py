import sys


def main():
    index = 0

    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "r") as file:
                index = process_stream(file, index)
    else:
        process_stream(sys.stdin)


def process_stream(stream, index=0):
    for line in stream:
        index += 1
        print(f"{format_index(index)} {line}", end="")

    return index


def format_index(index):
    return "{:>6} ".format(str(index))


if __name__ == "__main__":
    main()
