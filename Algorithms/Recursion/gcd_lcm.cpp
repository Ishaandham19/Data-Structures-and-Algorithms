#include <iostream>
#include <cstdlib>

//using iteration  O(n)
int gcdBad(int x, int y) {
	int range = x > y ? x : y;
	int gcd = 0;
	for (int i = 1; i <= range; i++) {
		if (x % i == 0 && y % i == 0)
			gcd = i;
	}

	return gcd;
}

//Using Euclid's GCD algorithm
int gcd(int x, int y) {
	if (x == 0 || y == 0) return 0;
	if (x % y == 0)
		return y;
	else
		gcd(y, x % y);
}

int lcm(int x, int y) {
	// GCD * LCM = Product   (proof using number theory)
	if (x == 0 || y == 0) return 0;

	return x * y / gcd(x, y);
}

int main() { 
	//stress test
	/*
	while (true){
		int num1 = rand() % 10000000 + 1;
		int num2 = rand() % 10000000 + 1;
		std::cout << "gdc" << ' ' << "gcdBad" << std::endl;
		std::cout << gcd(num1, num2) << ' ' << gcdBad(num1, num2) << std::endl;
		if (gcd(num1, num2) != gcdBad(num1, num2))
			std::cout << "Error";
	}
	*/
	int x = 0, y = 0;
	while (std::cin >> x >> y)
		std::cout << "lcm" << lcm(x,y) << std::endl;

	return 0;
}
