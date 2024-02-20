```bash
$ python3 tail.py artifacts/tail/example-text.txt
11
12
13
14
15
16
17
18
19
20
$ python3 tail.py artifacts/tail/example-text.txt artifacts/tail/example-text.txt
==> artifacts/tail/example-text.txt <==
11
12
13
14
15
16
17
18
19
20

==> artifacts/tail/example-text.txt <==
11
12
13
14
15
16
17
18
19
20
$ cat artifacts/tail/example-text.txt | python3 tail.py
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
$ diff <(python tail.py artifacts/tail/example-text.txt artifacts/tail/example-text.txt) <(tail -n 10 artifacts/tail/example-text.txt artifacts/tail/example-text.txt); echo $?
0
```
