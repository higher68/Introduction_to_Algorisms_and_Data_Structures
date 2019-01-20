#include<iostream>
using namespace std;
static const int MAX = 100;
static const int INFTY = (1<<21);
static const int WHITE = 0;
static const int GRAY = 1;
static const int BLACK = 2;

int n, M[MAX][MAX];

int prim() {
  int u, minv;
  int d[MAX], p[MAX], color[MAX];

  // d[v]：Tに属する頂点とV-Tに属する頂点を繋ぐ辺で、重みが最小の辺の重みを格納
  // p[v]：MSTにおける頂点vの親を記録
  // color[v]：vの訪問状態を記録。whiteはまだ、grayはそこにいる。blackは訪問済み
  // M[u][v]：uからvへの辺の重みを記録した隣接行列

  // 重みの初期値(最小を求めるのでinf, 頂点の親の初期値, colorの初期値設定)
  for ( int i = 0; i < n; i++) {
    d[i] = INFTY;
    p[i] = -1;
    color[i] = WHITE;
  }

  d[0] = 0;

  while (1) {
    minv = INFTY;
    u = -1;
    for (int i = 0; i < n; i++) {
      if (minv > d[i] && color[i] != BLACK ) {
        u = i;
        minv = d[i];
      }
    }
    if (u == -1) break;
    color[u] = BLACK;
    for (int v = 0; v < n; v++ ){
      if (color[v] != BLACK && M[u][v] != INFTY) {
        if ( d[v] > M[u][v] ) {
          d[v] = M[u][v];
          p[v] = u;
          color[v] = GRAY;
        }
      }
    }
  }
  int sum = 0;
  for (int i = 0; i < n; i++) {
    if (p[i] != -1) sum += M[i][p[i]];
  }

  return sum;
}

int main() {
  cin >> n;

  for (int i = 0; i < n; i++ ){
    for ( int j = 0; j < n; j++){
      int e;
      cin >> e;
      M[i][j] = (e == -1) ? INFTY : e;
    }
  }
  cout << prim() << endl;

  return 0;
}



