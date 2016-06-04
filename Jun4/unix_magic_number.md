## Magic Number
It is a constant numerical value used to identify a file format of protocol. [List of signatures](https://en.wikipedia.org/wiki/List_of_file_signatures) of different file formats.

#### Portable Network Graphics
```
89 50 4E 47 0D 0A 1A 0A
```

After the header comes a series of chunks. Chunk is a fragment of information.


#### Joint Phorographic Experts Group
```
FF D8 FF
```

JPEG consists of a sequence of segments, each beginning with a marker, each of which begins with a `0xFF` byte followed by a byte indication what kind of marker it is. Consecutive `0xFF` bytes are used as a fill bytes for padding purposes.

```
0xFF, 0xD8	variable	Start of image
0xFF, 0xC0	variable	Start of frame; baseline
0xFF, 0xC2	variable	Start of frame; progressive
0xFF, 0xC4	variable	Define Huffman table
0xFF, 0xDB	variable	Define quantization table
0xFF, 0xDD	4 bytes		Define restart interval
0xFF, 0xDA	variable	Start of scan; baseline - single scan
0xFF, 0xDn	(n=0..7)	Restart
0xFF, 0xEn	variable	Application specific
0xFF, 0xFE	variable	Text comment
0xFF, 0xD9	none		End of image
```