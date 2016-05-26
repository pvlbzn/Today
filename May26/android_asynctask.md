## `AsyncTask`
The whole thing is about that process processes on UI thread, which is a main thread, which arent executed immediately is a *super* bad idea.

> [`AsyncTask`](https://developer.android.com/reference/android/os/AsyncTask.html) enables proper and easy use of the UI thread. This class allows to perform background operations and publish results on the UI thread without having to manipulate threads and/or handlers.

`AsyncTask` should be used for a short operations, **a few seconds at the most**. For longer tasks use `java.util.concurrent` package. More info about [Processes and Threads](https://developer.android.com/guide/components/processes-and-threads.html).

An asynchronous task is defined by a computation that runs on a background thread and whose result is published on the UI thread.

3 generic types:

- `Params`
- `Progress`
- `Result`

And 4 steps:

- `onPreExecute`
- `doInBackground`
- `onProgressUpdate`
- `onPostExecute`

To receive back a `Result` you can use `.get` method, however it **blocks** until `AsyncTask` will be done, which is weird.


#### Android Ports
Not really about `AsyncTask`, however this behaviour was firstly encountered in `AsyncTask`. AVD, seems, always uses a new port because of some reason.


#### Execution

`onPreExecute` invoked on the **UI thread** before the task is executed.

`doInBackground` invoked on the background thread immediately after `onPreExecute`. The `Params` are passed to this step. The `Result` mus be returned by this step and will be passed back to the last step. `publishProgress` can be used here.

`onProgressUpdate` invoked on the UI thread after a call to `publishProgress`.

`onPostExecute` invoked on the UI thread after the background computation finishes. The result of the background computation is passed to this step as a parameter.


#### Rules

- `AsyncTask` class must be loaded on the UI thread.
- The task instance must be created on the UI thread.
- `execute()` must be invoked on the UI thread.
- Do not call any of `AsyncTask` methods manually.