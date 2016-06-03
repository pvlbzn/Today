#### `hexdump`
`hexdump` prints byte array to console. It can be piped into a file to further explorations.

```
$ hexdump filename.format > dump.txt
```

### Binary as Image
This thick is simple and impressive. The idea is to represent binary as an image. This task can be achieved using a PGM type.

```
$ (echo "P5 512 4096 255"; cat filename.jpg) > filename.pgm
```

First write a header, where is 512 is a width, 4096 is a length. After the header get a raw file representation and pipe it into the `.pgm`. `.pgm` can be opened in linux by default, or on other systems using some software such as Photoshop or Gimp.

