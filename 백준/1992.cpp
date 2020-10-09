#include <stdio.h>
using namespace std;
int mat[65][65];

void func(int c, int r, int size) {
	int cur = mat[r][c];
	bool same = true;
	for (int i = r; i < r + size; i++) {
		for (int j = c; j < c + size; j++) {
			if (cur != mat[i][j]) same = false;
		}
	}
	if (same) printf("%d", cur);
	else {
		printf("(");
		func(c, r, size / 2);
		func(c + size / 2, r, size / 2);
		func(c, r + size / 2, size / 2);
		func(c + size / 2, r + size / 2, size / 2);
		printf(")");
	}
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%1d", &mat[i][j]);
		}
	}
	func(0,0,n);
}