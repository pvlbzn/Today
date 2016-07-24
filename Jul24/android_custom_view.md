## Custom View
There are two approaches to create a new view.

- Extend an existing view
- Extend View class and build a new view from scratch

A good custom view must follow design principles:

- Conform to Android standards
- Provide custom styleable attributes that work with XML layouts
- Send accessibility events
- Be compatible with multiple Android platforms

Every standard view inherits from `View` class, thus to create a custom view the `View` should be extended.

```
/**
 * Constructor.
 *
 * @param context - interface to global information about an app
 *                  environment.
 * @param attrs - collection of attributes, as found associated
 *                with a tag in an XML document.
 */
public PieChart(Context context, AttributeSet attrs) {
    super(context, attrs);
}
```

To add your view to user interface you specify it in an XML element and controll its apperance and behaviour with element attributes. To enable this behavior in your custom view:

- Define custom attributes for your view in a `<declare-styleable>` resource element
- Specify values for the attributes in your XML layout
- Retrieve attribute values at runtime
- Apply the retrieved attribute values to your view

### Define
To define custom attrs `<declare-styleable>` should be added to resources `res/values/attrs.xml` in a way:

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <declare-styleable name="ClassName">
        <attr name="doOrNot" format="boolean" />
        <attr name="placeWhere" format="enum">
            <enum name="left" value="0" />
            <enum name="right" value="1" />
        </attr>
    </declare-styleable>
</resources>
```

New attributes belongs to a new namespace `http://schemas.android.com/apk/res/yourPackageName`, not to `http://schemas.android.com/apk/res/android`. Alias can be choosed using this derective `xmlns:anAlias="http://schemas.android.com/apk/res/yourPackageName"`.


### Apply
When a view is created from an XML layout, all of the attrs in the XML tag are read from the resource bundle and passed into the view's constructor as an `AttributeSet`.
Recommended way to read values from `AttributeSet` is to pass it to `obtainStyledAttrubutes()`.
