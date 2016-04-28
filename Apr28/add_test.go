package add

import "testing"

func TestAddOne(t *testing.T) {
	cases := []struct {
		in, out int
	}{
		{5, 6}, {7, 8}, {10, 11},
	}
	for _, c := range cases {
		got := AddOne(c.in)
		if got != c.out {
			t.Errorf("AddOne(%q) == %q, want %q", c.in, got, c.out)
		}
	}
}
