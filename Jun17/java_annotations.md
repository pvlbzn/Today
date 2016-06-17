## @
Anotations is a form of metadata. It provide data about a program that is not part of the profram itself. Annotations have no direct effect.

#### Use

- Instructions to the compiler
- Compile-time instructions
- Runtime instructions

Java has three built-in annotations: `@Deprecated`, `@Override`, `@SuppressWarnings`. Annotations can be applied to the class, interface, mathod, field.


#### Override
While overriding a method in the child class `@Override` should be used. This practice helps in avoiding a maintance issues such as changed method signature of parent class. This is difficult to trace when annotations were skiped.

#### Deprecated
Indicates that the marked element is deprecated and should no longer be used.

#### SuppressWarnings
Annotation instructs compiler to ignore specific warnings like use of deprecated things. Syntax is `@SuppressWarnings("deprecation")`.

