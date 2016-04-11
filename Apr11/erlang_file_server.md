####File server
The basic unit of concurrency in Erlang is the *process*. *Process* is a lightweight VM that communicates by sending and receiving messages.

**File server process**
The code for a process is contained in a module, to create a process we call `spawn()`.

```
-module(fs). 
-export([start/1, loop/1]). 

start(Dir) ->
	spawn(fs, loop, [Dir]). 

loop(Dir) ->
	receive
		{Client, list_dir} ->
			Client ! {self(), file:list_dir(Dir)};
		{Client, {get_file, File}} ->
			Full = filename:join(Dir, File),
			Client ! {self(), file:read_file(Full)}
	end,
	loop(Dir). 
```

This is how to write infinite loop. The `Dir` contains the cwd of the file server. In the loop we wait to receive a command; when we receive a command, we obey the command and then call ourselves again to get the next one.

Erlang applies a *tail-call* optimization, which means that this function will run in constant space. No stackoverflow.

If program receive the message `{Client, list_dir}`, it should reply with a list of files. If program receive the message `{Client, {get_file, File}}`, it should reply with the file. The variable `Client` becomes bound as part of the pattern matching process that occurs when a message is received.

*Who to reply to*: `Client` is the PID of the process that sent the request, thus to who, the reply should be sent.

*Use if self()*: Reply sent by the server contains the arg self(), which is this case PID of the server. This PID is added to the message, so client can check that the message is from server, not from other process.

*Pattern matching*: is used to select the message. 

```
receive
	Pattern1 ->
		Actions1;
	Pattern2 ->
		Action2;
	...
end
```

Thus, there are no if-then-else, switch statements.

**Client**: is actually symetrical

```
ls(Server) ->
	Server ! {self(), list_dir},
	receive
		{Server, FileList} ->
			FileList
	end.

get_file(Server, File) ->
	Server ! {self(), {get_file, File}},
	receive
		{Server, Content} ->
			Content
	end.
```

Pattern:

```
receive
	{Client, Pattern} ->
		...
end
```

