###How to font

Android shiped with awesome font "Roboto" and, well, a 'limited documentation':

[!Roboto Font](https://material-design.storage.googleapis.com/publish/material_v_4/material_ext_publish/0Bx4BSt6jniD7SW9CUzR4MnRpOTg/style_typography_roboto1.png)

Here is design [guidelines](https://www.google.com/design/spec/style/typography.html#typography-styles), but no API doc.

<br>

####Open Source

Android is an open source project, thus here is `platform/frameworks/` [implementation](https://android.googlesource.com/platform/frameworks/base/+/master/data/fonts/system_fonts.xml) called `system_fonts`.

```
android:fontFamily="sans-serif"           // roboto regular
android:fontFamily="sans-serif-light"     // roboto light
android:fontFamily="sans-serif-condensed" // roboto condensed
android:fontFamily="sans-serif-thin"      // roboto thin (android 4.2)
android:fontFamily="sans-serif-medium"    // roboto medium (android 5.0)
```

And different flavours:

```
android:textStyle="normal|bold|italic"
```


