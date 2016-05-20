### Spark Framework

`Spark` - Sinatra inspired framework for Java, as states github page of the Spark. I choose Spark because it is a tiny framework what automatically makes it easier to understand how it works, why it works, what it does. Also, it will be interesting to compare Spark to Sinatra, because Sinatra was a first web thing I touched.

The purpose of this series on Spark:

- Understand how Java plays in web frameworks world
- Try Java flawored framework
- Make some study on frameworks in general

Last point is truly not least because I prefer, especially while learning, to not use frameworks for everything and I'm not a fan of frameworks approach in big picture. Instead of learning how web (and things) works people are learning web frameworks. Okey. So this will be a first spin into Java frameworks and will be a first attempt to understand the framework. Before begin, I checked a source code, it looks legit.


### Build Tools

To add some dependencies you have to use one of the build tools. Short research shows that there are a lot of build tools around and it seems that the winner is Gradle build tool. It is a build tool with its own domain specific language instead of XML or another markup language.

Spark tutorial uses a Maven build system. There is also a thing called Maven Central. This is a java's kind of pip or gem or whatever.

Maven can "prepare" your new directory for a project using cli or plugin in IDE. After you create a new project, you have a bloat like folders and xml files without even writing a line of code!

All settings are hanging in `pom.xml` with following structure:

```
<dependencies>
    <dependency>
        <groupId>com.sparkjava</groupId>
        <artifactId>spark-core</artifactId>
        <version>2.5</version>
    </dependency>
</dependencies>
```

This works well and actually this is a convinient way to deal with dependencies.

*There will be another documents for a build tools because it is a massive topic.*
