#include <iostream>
#include <vector>
#include <cstdlib>

using std::vector;
using std::cout;
using std::cin;

int fibonacciBad(int n) {
	if (n <= 1) return n;
	else return fibonacciBad(n - 1) + fibonacciBad(n - 2);
}

int fibonacci(int n) {
	if (n <= 0) return 0;
	vector<int> series(n+1);
	series[0] = 0;
	series[1] = 1;

	for (int i = 2; i <= n; i++) {
		series[i] = series[i - 1] + series[i - 2];
	}

	return series[n];
}

int main() {
	/*stress test
	int x = 0;
	while (true) {
		x = rand() % 20;
		int fib1 = fibonacciBad(x);
		int fib2 = fibonacci(x);
		cout << fib1 << ' ' << fib2 << std::endl;
		if (fib1 != fib2) {
			cout << "Error!" << "\n";
			break;
		}
	}
	*/

	//displays fib(n)
	int n = 0;
	cin >> n;
	cout << fibonacci(n);
}
