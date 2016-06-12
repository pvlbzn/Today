## Reflection
How to violate private fields of the class.

Consider following class with two private fields `str` and `num`.

```
public class Target {

    private String str;
    private int num;

    public String getStr() {
        return str;
    }

    public int getNum() {
        return num;
    }
}
```

Access to private fields from another class:

```
public class Reflector {

    public static void main(String[] args) {
        try {

            Target t = new Target();
            Field f = t.getClass().getDeclaredField("str");
            f.setAccessible(true);
            String s = "Hello";
            f.set(t, s);
            System.out.println(t.getStr());

        } catch (NoSuchFieldException err) {}
          catch (IllegalAccessException err) {}
    }
}
```

This stuff is a *reflection*. This is a way how, for example, `Gson` library works. It access private fields without accessors.