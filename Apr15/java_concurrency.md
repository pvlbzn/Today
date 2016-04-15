###Java Concurrency

Some links to go:

- [Doug Lea](http://g.oswego.edu/)
- [Concurrency in Practice](http://www.amazon.com/Java-Concurrency-Practice-Brian-Goetz/dp/0321349601/ref=pd_bxgy_14_img_2?ie=UTF8&refRID=0Q7T96ASEMM9NQ7PQ911)
- [Dosc Oracle](https://docs.oracle.com/javase/tutorial/essential/concurrency/index.html)


####Why?
I want to learn concurrency from a different perspective. In past weeks I did it with Erlang, Python and now I'm goign to do some concurrency using Java. I tried Erlang because of functional programming as a major reason, I'm not going to dive deep enough in this month. Python has a weird story with a concurrency. Thanks to awesome Python community, there are a lot, truly alot of materials on Pythons concurrency model, C extentions, CPython implementation (with GIL 'side-effect'). Now I want to dig deeper into concurrency practice, without GIL limitations and greenlets, gevent and other stuff. Also, I have some Java skills, so there is no need to learn language from a ground up.

<br>

####Java Concurrency Primitives
Java has the low-level concurrency primitives: `synchronized`, `valotile`, `wait()`, `notify()`, `notifyAll()`. As documentation states, these primitives can be tricky in use.

####Concurrency Utilities
As documentation sudgests: use concurrency utilities `java.util.concurrent` package.

####A Little Note
During this project, there will be such days, where learning material is not suitable to note-taking format, like now. When you learn complitely new concepts, it is not always sane to conspect and note everything, however most of the 'dig deeper' stuff is prety much noteable.
