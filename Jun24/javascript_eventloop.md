## Execution Lifecycle

```
Stack ---------> Queue
  ^                |
  |                v
  +--- EventLoop --+
```

When a function is called it is pushed onto the stack, this frame pushed onto the stack. Frame contains argumens and local variables. When function returns, the top frame evement is popped out of the stack.

JS runtime contains a message queue, which is a list of messages ot be processed. When the **stack is empty**, a message is taken out of the queue and processed. The message processing ends when the stack becomes empty again.

#### Event Loop
Event loop is a loop because:

```
while (queue.waitForMessage()) {
    queue.processNextMessage();
}
```

`queue.waitForMessage` waits synchronously for a message to arrive if there is none currently. Each message is processed completely before any other message is processed. It means that function is always completes, unlike C, where if a function runs in a thread, it can be stopped to run other code in another thread. If function takes too long time it freezes an UI.

#### Adding Messages
In web browsers, messages are added any time an event occurs and there is an event listener attached to it. `setTimeout` will add a message to the queue. If there is no message in the queue and the stack is empty, the message is processed right away.

```
(function() {
    console.log('1');

    setTimeout(function() {
        console.log('timeout');
    }, 0);

    console.log('2');
})();
```

Will print `1`, `2`, `timeout`. `timeout` will arrive the last one because `setTimeout` will be queued and executed only when the stack will be empty. Execution flow: first console log call pushed onto the stack, executed. `setTimeout` added to the message queue. Second console log is pushed onto the stack, executed, returns. Stack is empty and the queued message will be processed.