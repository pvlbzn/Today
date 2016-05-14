#### Code Block

Java has a not wide used and wide known property as a plain code block in the other block.

```
class WhateverClass {

    {
        // This code block will be executed as class
        // will be initialized.
    }

    // Constructors

    // Methods
}
```

I already mentioned [this](https://github.com/pvlbzn/Today/blob/d112c698b6c2a167f1b166ba9e7206bc3b75521d/Apr16/java_code_block_this.md) property, however today I first time found a usecage of it. Here is a code snippet from `InteAddress.java`, it uses a static modifier because it is in a static class:

```
/*
 * Load net library into runtime, and perform initializations.
 */
static {
    preferIPv6Address = java.security.AccessController.doPrivileged(
        new GetBooleanAction("java.net.preferIPv6Addresses")).booleanValue();
    AccessController.doPrivileged(
        new java.security.PrivilegedAction<Void>() {
            public Void run() {
                System.loadLibrary("net");
                return null;
            }
        });
    init();
}
```
