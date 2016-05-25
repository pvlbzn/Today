## Build Tool

*This topic was started few days ago [here]. This doc will be about Gradle only.*

Gradle can be used for JVM language or for C and C++.


#### Daemon
Gradle has a daemon - a long-lived backgroud process. The purpose of it is straightforvard: Gradle runs on JVM and uses supporting libs, all these stuff require time to cold-start. It just make every single start faster.

In `.gradle/gradle.properties` modify (or add) `org.gradle.daemon=true`.

Every Daemon stops after 3 hours of inactivity. In order to stop it manualy use `gradle --stop`.


#### Plugins
Because of most projects have the similar boiler plate code and builds, Gradle can generate it using plugins. One of these - [Java plugin](https://docs.gradle.org/current/userguide/java_plugin.html). This plugin in "convention based", which means that you don't have to do much as long as you follow the rules.

To generate folder use

```
gradle init --type java-library
```

It will setup project as well as add `java-plugin` to the project.