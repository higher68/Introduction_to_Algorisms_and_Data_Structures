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

  // 同じindex、つまり行列1個の場合はコスト0
  for (int i = 1; i <= n; i++) m[i][i] = 0;
  // 計算する行列積の長さでループ
  for (int l = 2; l <= n; l++) {
    // 計算し始める行列の始点をずらす
    for (int i = 1; i <= n -l + 1; i++ ) {
      int j = i + l - 1;
      // 1 の 21bit左シフト。要するにinfty
      m[i][j] = (1 << 21);
      for (int k = i; k <= j - 1; k++) {
        m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + p[i - 1] * p[k] * p[j]);
      }
    }
  }

  cout << m[1][n] << encl;

  return 0;
}

