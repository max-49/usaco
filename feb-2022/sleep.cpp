#include <bits/stdc++.h>
using namespace std;

int main() {
	int T; cin >> T;
	vector<int> x(N), y(N);
	for (int& t: x) cin >> t;
	for (int& t: y) cin >> t;
	int max_square = 0;
	for (int i = 0; i < N; i++) { // for each first point
		for (int j = i+1; j < N; j++) { // for each second point
			int dx = x[i]-x[j], dy = y[i]-y[j];
			int square = dx*dx+dy*dy;
			// if the square of the distance between the two points is greater than
			// our current maximum, then update the maximum
			max_square = max(max_square,square);
		}
	}
	cout << max_square;
}