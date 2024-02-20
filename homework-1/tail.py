import sys


def main():
    if len(sys.argv) > 1:
        files_count = len(sys.argv) - 1
        print_filename = files_count > 1

        for index, filename in enumerate(sys.argv[1:]):
            with open(filename, "r") as file:
                process_stream(
                    file,
                    print_filename=print_filename,
                    last_entry=index == files_count - 1,
                )
    else:
        process_stream(sys.stdin, lines_count=17)


def process_stream(stream, lines_count=10, print_filename=False, last_entry=False):
    buffer = []
    for line in stream:
        buffer.append(line)
        if len(buffer) > lines_count:
            buffer = buffer[1:]

    if print_filename:
        print("==> %s <==" % stream.name)

    for line in buffer:
        print(line, end="")

    if not last_entry and print_filename:
        print("")


if __name__ == "__main__":
    main()
