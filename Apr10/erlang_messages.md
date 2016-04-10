###Messages
**Sending Messages**
In Erlang, processes share no memory and can interact only with each other by sending messages.

```
PID ! {self(), MsgString}
```

this means send the message in {} to the process PID, `self()` is a sender, `MsgString` is a message string.


**Receiving Messages**

```
receive
	{From, Message} ->
		...
end
```

When a PID (from sending messages) receives a message, the variable `From` will be bound to `self()` from sending message, `Message` will contain message.
