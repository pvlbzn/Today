## Performance
JS performance perhaps is more interesting topic than, say, Python performance because of many reasons. Besides a clear distinction like Python actually use types, or a complitely different execution enviroment, JS performance difference may vary between Python and C++, while Python's performance may vary between a slow Python and a fast Python, but not even close to C++.

Difference is huge and a good idea is to learn about it. Also it is not about 'premature optimizations' it is about how to white code for V8. Also, V8 constantly involves and some of the issues which can be founded in the internet aren't actual any more.

#### D8
D8 is a V8's shell. In order to use properly some setups, like installing `depot_tools`,  must be [done](https://github.com/v8/v8/wiki/Building%20with%20Gyp). After successful fetching and building D8 can be used. The process can be tricky, better to follow wiki carefully.

```
// cd to v8/out/Debug
./d8 --prof path/to/file.js

// It will produce a v8.log
// cd to v8/tools. v8.log will be in out/Debug directory.
./linux-tick-proccessor path/to/v8.log
```

Or plot it.

```
// From v8 directory
./out/Debug/d8 --prof --log-timer-events /path/to/file.js
./tools/plot-timer-events ./out/Debug/v8.log
```
This code will generate (gnuplot is required) `timer-events.png` in the current directory.

The `timer-events.png` from `./perf.js`:


