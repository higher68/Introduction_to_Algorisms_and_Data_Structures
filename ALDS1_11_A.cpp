#include<iostream>
using namespace std;
static const int N = 100;

int main() {
  int M[N][N];  // 0 オリジンの隣接行列
  int n, u, k, v;

  cin >> n;
  
  // initial condition insert
  for (int i = 0; i < n; j++) {
    for(int j = 0; j < n; j++) M[i][j] = 0;
  }

  for (int i = 0; i < n; i++)


