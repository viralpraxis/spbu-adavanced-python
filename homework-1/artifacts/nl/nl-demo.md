```bash
viralpraxis@primary:~/Documents/spbu/2024-spring/advanced-python/spbu-adavanced-python/homework-1$ python nl.py nl.py
     1  import sys
     2
     3
     4  def main():
     5      index = 0
     6
     7      if len(sys.argv) > 1:
     8          for filename in sys.argv[1:]:
     9              with open(filename, "r") as file:
    10                  index = process_stream(file, index)
    11      else:
    12          process_stream(sys.stdin)
    13
    14
    15  def process_stream(stream, index=0):
    16      for line in stream:
    17          index += 1
    18          print(f"{format_index(index)} {line}", end="")
    19
    20      return index
    21
    22
    23  def format_index(index):
    24      return "{:>6} ".format(str(index))
    25
    26
    27  if __name__ == "__main__":
    28      main()
```
