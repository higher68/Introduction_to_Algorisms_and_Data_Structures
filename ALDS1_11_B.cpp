#include<stdio.h>
#define N 100
#define WHITE 0
#define GRAY 1
#define BLACK 2

int n, M[N][N]
int color[N], d[N], f[N], tt;

// 再帰関数による深さ優先探索
void dfs_visit(int u) {
  int v;
  color[u] = GRAY;
  d[u] = ++tt; // 最初の訪問
  for (v = 0; v < n; v++) {
    if ( M[u][v] == 0)  continue;
    if (color[v] == WHITE ) {
      dfs_visit(v);
    }
  }
  color[u] = BLACK;
  f[u] = ++tt // 訪問の完了
}
