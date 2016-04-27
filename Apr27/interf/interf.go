// First touch to interfaces and packaging

package intertouch

import "math"

type GeoForm interface {
	Perimeter() float64
}

type Rect struct {
	Color  string
	Width  float64
	Height float64
}

type Circle struct {
	Color  string
	Radius float64
}

// Implement GeoForm interface on Rect struct
func (r Rect) Perimeter() float64 {
	return 2*r.Width + 2*r.Height
}

// Implement GeoForm interface on Circle struct
func (c Circle) Perimeter() float64 {
	return math.Pi * c.Radius * c.Radius
}
