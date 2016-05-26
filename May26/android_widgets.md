## android.widget

*It's hard to find appropriate info about widget, good example of a name collision.*

[`widget`](https://github.com/android/platform_frameworks_base/tree/master/core/java/android/widget) is a package which contains UI elements. Developers can create custom `widget`.

Examples: [`TextView`](https://github.com/android/platform_frameworks_base/blob/master/core/java/android/widget/TextView.java) is (as I understand) symlink to `android.widget.TextView`. 

#### Custom `widget`
Your widget has to extend `View` or subclass of it. In orger to use in XML, there should be additional files.

- Java implementation file
- XML definition file
- Layout XML

An example of custom `widget` is in `android-apidemos`:

- [`LabelView.java`](https://github.com/appium/android-apidemos/blob/master/src/io/appium/android/apis/view/LabelView.java)
- [`res/values/attrs.xml`](https://github.com/appium/android-apidemos/blob/master/res/values/attrs.xml)
- [`res/layout/custom_view_1.xml`](https://github.com/appium/android-apidemos/blob/master/res/layout/custom_view_1.xml)