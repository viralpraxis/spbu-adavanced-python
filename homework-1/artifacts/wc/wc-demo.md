```bash
$ python wc.py artifacts/wc/lorem.txt
  26 1002 5999 artifacts/wc/lorem.txt
$ python wc.py artifacts/wc/lorem.txt artifacts/wc/lorem.txt
   26  1002  5999 artifacts/wc/lorem.txt
   26  1002  5999 artifacts/wc/lorem.txt
   52  2004 11998 total
$ cat artifacts/wc/lorem.txt | python wc.py
  26 1002 5999
```
