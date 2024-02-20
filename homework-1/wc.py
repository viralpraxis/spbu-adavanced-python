import sys


def main():
    if len(sys.argv) > 1:
        files_count = len(sys.argv) - 1

        total_lines, total_words, total_chars = 0, 0, 0
        entries = []

        for filename in sys.argv[1:]:
            with open(filename, "r") as file:
                lines, words, chars = process_stream(file)
                total_lines += lines
                total_words += words
                total_chars += chars

                entries.append([filename, lines, words, chars])

        for filename, lines, words, chars in entries:
            print_entry(filename, lines, words, chars, rjust=len(str(total_chars)))

        if files_count > 1:
            print_entry(
                "total",
                total_lines,
                total_words,
                total_chars,
                rjust=len(str(total_chars)),
            )
    else:
        print_entry("", *process_stream(sys.stdin))


def process_stream(stream):
    lines, words, chars = 0, 0, 0

    for line in stream:
        chars += len(line)
        words += len(line.split())
        lines += 1

    return lines, words, chars


def print_entry(filename, lines, words, chars, rjust=None):
    if rjust is None:
        rjust = len(str(chars))

    print(
        "%s %s %s %s"
        % (
            str(lines).rjust(rjust),
            str(words).rjust(rjust),
            str(chars).rjust(rjust),
            filename,
        )
    )


if __name__ == "__main__":
    main()
