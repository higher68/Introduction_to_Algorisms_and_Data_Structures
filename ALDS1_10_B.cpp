#include<iostream>
#include<algorithm>
using namespace std;

static cost in N = 100;

int main() {
  int n, p[N+1], m[N+1][N+1];
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> p[i-1] >> p[i];
  }

  for (int i = 1; i <= n; i++) m[i][i] = 0;
  for (int l = 2; l <= n; l++) {
    for (int i = 1; i <= n -l + 1; i++ ) {

