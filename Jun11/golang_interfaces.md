## Interface
Interface is a two things:

- Set of methods
- Type


#### Method Aspect
```
type Vehicle interface {
	Ride() int
}

type Bicycle struct {
}

type Golfcar struct {
}

type Jeep struct {
}

func (b Bicycle) Ride() int {
	return 18
}

func (g Golfcar) Ride() int {
	return 25
}

func (j Jeep) Ride() int {
	return 140
}

func main() {
	rides := []Vehicle{Bicycle{}, Golfcar{}, Jeep{}}
	for _, ride := range rides {
		fmt.Println(ride.Ride())
	}
}
```

#### `interface{}` type
*The empty interface*. The `interface{}` type is the interface with no methods in it. Golang has no *implements* keyword, thus all types, at least, implements zero methods and sutisfying of `interface{}` is done automatically. Yes, **all the types implement the empty interface**.

```
func Function(v interface{}) {
	/*
	Will accept any parameter. However it doesn't mean any type.
	Type is interface{}. When passign a value here, the Go runtime
	will perform type conversion, and convert any `v` to the empty
	interface type. All values have exactly one type at the runtime.
	*/
}
```

An interface value is constructed of two *words*. First is used to point to a method table for the underlying type. Second is used to point to the actual data held by the value.


TODO: Read [Go Data Structures: Interfaces](http://research.swtch.com/interfaces).
