## Serialization
Serialization is the process of translating data structures into a format that can be stored and reconstructed later. The process of serializing an object is also called marshalling an object. Opposite operation is deserealization or unmarshalling.

Many languages (platforms) have object serialization built-in or using library, framework (such as google's protobuf), or just serialization functions. 

From Google Protocol Buffers docs, **note**:
>Use Java Serialization. This is the default approach since it's built into the language, but it has a host of well-known problems (see Effective Java, by Josh Bloch pp. 213), and also doesn't work very well if you need to share data with applications written in C++ or Python.

TODO: [Protocol Buffer Basics: Java](https://developers.google.com/protocol-buffers/docs/javatutorial).


### Novadays
Todays most common serialization formats are JSON and XML.


### Java Serialization
Java provids a mechanism, called object serialization, where an obect can be represented as a sequence of bytes that includes the object's data as well as information about the object's type and the types of data stored in the object.

To *serialize* an object means to convert its state to a byte stream.

```
public class Data implements Serializable {

  private String mStr = "This value will be serialized";
  private int    mInt = 34634;

  private transient List<Integer> goingToStay;

  public static void main(String[] args) throws IOException {
    // Declare and initialize new Data instance.
    Data instance = new Data();

    // OOS class have the default
    ObjectOutputStream oos = new ObjectOutputStream(
        // By using FOS we will Write it to a File in the file
        // system. It could have been a Socket, a database, in
        // memory array.
        new FileOutputStream(new File("sample.ser"))
    );

    oos.writeObject(instance);
    oos.close();
  }

}
```

This will produce sample.ser binary, where `instance` is written.