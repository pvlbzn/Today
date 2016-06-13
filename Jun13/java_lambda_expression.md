## Lambda
*Lambda expression*, also called *anonymous function* or *function literal* is a function which doesn't bound to an identifier.

#### Lambda or Closure
A *closure* in a *lambda expression* paired with an environment that bings each of its free variables to a value. Thus, the closure is an implementation techinique.

#### Why
Abstraction over behavior. Lambda is about *what* computation should be performed rather than *how* it should be performed.


#### Android Example

Declate and initialize object:

```
FloatingActionBar fab = (FloatingActionBar) findViewById(R.id.fab);
```

Standard approach:

```
fab.setOnClickListener(new View.OnClickListener() {
	@Override
	public void onClick(View v) {
		// Do
	}
}
})
```

The same using lambda expression:

```
fab.setOnClickListener((View v) -> {
	// Do
})
```
