# DS_Store Analyser 🧐

> Dowload and Run:
```
➜ git clone https://github.com/phor3nsic/dsstore_analyser.git
➜ cd dsstore_analyser && python3 -m pip -r requirements.txt
```

> Help:

```
➜ python3 dsstore.py -h

usage: dsstore.py [-h] [-f FILE] [-l URLLIST]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to the DS_Store file
  -l URLLIST, --urllist List of urls
```

##  Examples:

> Use List of urls:
```
➜ cat /tmp/urls.txt

http://example.com/.DS_Store
http://example2.com/.DS_Store
http://example3.com/.DS_Store

➜ python3 dsstore.py -l /tmp/urls.txt

```

> Use local file:
```
➜ python3 dsstore.py -f /tmp/.DS_Store

```