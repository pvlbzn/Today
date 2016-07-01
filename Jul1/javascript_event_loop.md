## Difference

Python

```
r = requests.get('https://example.com')
print(r.text)
print('done')

# Execution
> waits for response
> prints text
> prints done
```

Node

```
request('https://example.com', function (error, response, body) {
    console.log(body);
});
console.log('done');

// Execution
> function is executed, callback passed
> logs done
> logs body when it will be ready
```

## Event Loop
Where in memory do these callbacks live and what is an execution order? JS runtime contain a **message queue which stores a list of messages to be processed and their associated callback functions**. These messages are queued in response to external *events* (like receiving the response to an HTTP request) given callback function.

In a loop, the queu is polled for the next message (poll = tick) and when a message is encountered, the callback for that message is executed.

[!IMAGE](http://blog.carbonfive.com/wp-content/uploads/2013/10/event-loop.png)
*Source: [link](http://blog.carbonfive.com/2013/10/27/the-javascript-event-loop-explained/)*

