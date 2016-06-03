## Magic Number
It is a constant numerical value used to identify a file format of protocol. [List of signatures](https://en.wikipedia.org/wiki/List_of_file_signatures) of different file formats.

#### Portable Network Graphics
```
89 50 4E 47 0D 0A 1A 0A
```

#### Joint Phorographic Experts Group
```
FF D8 FF
```

JPEG consists of a sequence of segments, each beginning with a marker, each of which begins with a `0xFF` byte followed by a byte indication what kind of marker it is. Consecutive `0xFF` bytes are used as a fill bytes for padding purposes.

