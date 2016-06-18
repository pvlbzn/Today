## Custom Annotations

Annotations made by using `@interface` followed by name. Annotations extends `java.lang.annotation.Annotation` interface.

```
public @interface Copyright {
    String info() default "";
}
```

As a more usefull example: @Test reimplementation

```
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Test {
    Class expected();
}
```

`@Target` marks a target on an annotation. In this case the target is methods. If `@Target` does not specified, the anntotaion is welcome to use enywhere. `@Retention` specifies how to retaine annotation, particularly usefull for Java reflections.

#### Annotation Parser

The basic idea behind the annotation parser is using Java reflections to access the annotation attributes.

```
public class TestAnnotationParser {
    
    public void parse(Class<?> c) throws Exception {
        Method[] methods = c.getMethods();
        int pass = 0;
        int fail = 0;
        for (Method m : methods) {
            if (m.isAnnotationPresent(Test.class)) {
                Test test = m.getAnnotations(Test.class);
                Class exp = test.expected();
                try {
                    m.invoke(null);
                    pass++;
                } catch (Exception e) {
                    if (Exception.class != exp) {
                        fail++;
                    } else {
                        pass++;
                    }
                }
            }
        }
    }

}
```



#### Source
Learned from [isagoksu](http://isagoksu.com/2009/creating-custom-annotations-and-making-use-of-them/).
