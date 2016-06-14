## Android Support Library

Why? Short answer: use new features on the old devices.

developer.android.com states:

>The Android Support Library offers a number of features that are not built into the framework. These libraries offer backward-compatible versions of new features, provide useful UI elements that are not included in the framework, and provide a range of utilities that apps can draw on.

In an app calls one of the support class's methods, the support libary's behavior depends on what version of Android the app is running on. If the framework provides the necessary funtionaluty, the support lib calls on the framework to perform the task, else, the SL may try to provide the necessary functionality itself. So the doesn't need to check what version of Anroid it's running on. Instead, the app can rely on the SL to do those checks and choose appropriate behavior.

#### For What?
There are [**24, 093**](http://opensignal.com/reports/2015/08/android-fragmentation/) distinct Android devices which were seen this year (2015).

#### Libraries

[Full listing](https://developer.android.com/topic/libraries/support-library/features.html).

ASL was originally released in 2011 as Compatability Library. ASL isn't a single library, it is a collection of libraries, which can be divided into two groups:

- Compatability libs
- Components libs

#### Compatability Libraries
Compatability libraries focus on backporting features from newer framework releases.

**v4**: As name suggests, it supports back to API 4.

**v7-appcompat**: Back to API 7. It requires the **v4** but doesnt include it.

So, for example, if developer want to use Material UI, he/she will be forsed to use v4, because activity what is lower API 21 needs to extend `AppCompatActivity` which by itself extends `FragmentActivity`.

v4 and v7 are monoliths.

#### Component Library
Component libs are more modular, thus smaller. They enables developers to add features that, again, not part of the standard framework.

- cardview
- gridlayout
- mediarouter
- palette
- recyclerview

#### Other Libraries
There exists some other libraries, such as anotations or v17(for android TV).

#### What Does It Mean
Use support libs by default. It won't harm. Google consider the general use of the support libs to be a best practice.
