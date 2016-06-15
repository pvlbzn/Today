## Taxonomy

![Java Classes Taxonomy](https://mramabhadrarao.files.wordpress.com/2011/12/classtaxonomy.jpg)


#### Nested Classes

```
class C1 {
	class C2 {

	}
}
```

There are two types of nested classes:

- Non-static nested classes
- Static nested classes

#### Inner Classes

Inner class can be:

- Inner Classs
- Method-local Inner Class
- Anonymous Inner Class

**Inner Class**:

```
class Outer {
	
	private class Inner {
		public void print() {
			System.out.println("Inner.");
		}
	}

	void printInner() {
		Inner i = new Inner();
		i.print();
	}

}


public class C1 {
	
	psvm {
		Outer o = new Outer();
		o.printInner();
	}

}
```


**Method-local Inner Class**:

```
public class Outer {
	
	void method() {
		int n = 15;

		class MethodInner {
			public void print() {
				System.out.println("n is: " + n);
			}
		}

		MethodInner i = new MethodInner();
		i.print();
	}

	psvm() {
		Outer o = new Outer();
		o.method();
	}

}
```

After compilation this snipet will print "n is: 15".
This is really sick..


**Anonymous Inner Class**:
An inner class declared without a name is an anonymous inner class. These classes declared and instatiated at the same time.

```
abstract class Anonymous {
	public abstract void method();
}


public class Outer {
	psvm {
		Anonymous a = new Anonymous() {
			public void method() {
				System.out.println("Anonymous inner class");
			}
		}
		a.method();
	}
}
```

Or

```
interface Msg {
	String hello();
}


public class C1 {
	
	public void displayMsg(Msg m) {
		System.out.println(m.hello());
	}

	psvm {
		C1 obj = new C1();
		obj.displayMsg(new Msg() {
			public String greet() {
				return "Hi.";
			}
		});
	}

}
```
