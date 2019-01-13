#include<iostream>
using namespace std;
static const int N = 100;

int main() {
  int M[N][N];  // 0 オリジンの隣接行列
  int n, u, k, v;

  cin >> n;
  
  // initial condition insert
  for (int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) M[i][j] = 0;
  }

  for (int i = 0; i < n; i++) {
    cin >> u >> k;
    u--; // 0オリジンへ変換
    for (int j = 0; j < k; j++) {
      cin >> v;
      v--; // 0オリジンへ変換
      M[u][v] = 1; // uとvの間に辺を振る
    }
  }

  for (int i = 0; i < n; i++) {
    for ( int j = 0; j < n; j++) {
      if (j) cout << " "; // 最初以外は空白を前におく
      cout << M[i][j];
    }
    cout << endl;
  }
  
  return 0;
}

      

