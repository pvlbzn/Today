###RelativeLayout

RelativeLayout [implementation](https://android.googlesource.com/platform/frameworks/base/+/refs/heads/master/core/java/android/widget/RelativeLayout.java)

To arrange some element relative to another element, anchor view should be declared first, regardless of an actual position in a ViewGroup.

Screen:

```
Child1
Child2
```

XML:

```
RelativeLayout
	Child2
		id=child2
	Child1
		alignTop=child2
```

The point is that **id must be declared before use**. Sounds logical enough, however in XML layout it looks confusing. If Child1 will try to alignTop of the `child2` layout will produce an error.
