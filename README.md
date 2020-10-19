# Guido

Python CLI tool to compare files in two local directories, ignoring file extensions.

```
_                ___       _.--.
\`.|\..----...-'`   `-._.-'_.-'`
/  ' `         ,       __.--'
)/' _/     \   `-_,   /
`-'" `"\_  ,_.-;_.-\_ ',     fsc/as
    _.-'_./   {_.'   ; /
   {_.-``-'         {_/
```

# how to install

1. Download & install Python3: https://www.python.org/downloads/
2. Open terminal and run:

On Linux/MacOD:
```
pip install -U pip && pip install git+https://github.com/tomekzbrozek/guido.git
```

On Windows:
```
python3 -m pip install -U pip && pip install git+https://github.com/tomekzbrozek/guido.git
```


# how to use

pass full paths to folders A and B (two folders to compare)

```
guido -a /Users/tomaszzbrozek/folder1 -b /Users/tomaszzbrozek/folder2
```

For two folders like
```
folder1/
    cleo.csv
    heathcliff.json
    hector.csv
folder/2
    cleo.txt
    heathcliff.json
    riff-raff.txt
```

Guido will return the following results:

```
Files in /Users/tomaszzbrozek/folder1 that are not in /Users/tomaszzbrozek/folder2
    hector
Files in /Users/tomaszzbrozek/folder2 that are not in /Users/tomaszzbrozek/folder1
    riff-raff
```
