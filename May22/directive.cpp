#include <iostream>

#define get_max(x, y) (x>y?x:y)

int main() {
	int x = 15;
	int y = 25;
	std::cout << get_max(x, y) << std::endl;
}