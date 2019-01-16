#include<iostream>
#include<stack>
using namespace std;
static const int N = 100;
static const int WHITE = 0; // 未訪問の状態
static const int GRAY = 1; // 訪問中
static const int BLACK = 2; // 訪問済み

int n, M[N][N];
int color[N], d[N], f[N], tt;
int nt[N];            

// u に隣接するvを番号順に取得
int next(int u) {
  for ( int v = nt[u]; v < n; v++ ) {
    nt[u] = v + 1;
    if (M[u][v] ) return v;
  }
  return -1;
}

// スタックを用いた深さ優先探索
void dfs_visit(int r) {
  for (int i = 0; i < n; i++) nt[i] = 0;

  stack<int> S;
  S.push(r); // 始点uをスタックに追加
  color[r] = GRAY;
  d[r] = ++tt; // 訪問時刻を記載

  while (!S.empty() ) { // Sが空でない間
    int u = S.top(); // stackの一番上にある要素
    int v = next(u); 
    if ( v!= -1) {
      // topの隣に訪問していないものがあったら、スタックに追加
      if (color[v] == WHITE) {
        color[v] = GRAY;
        d[v] = ++tt;
        S.push(v);
      }
    } else {
      // topの隣が何もなかったら、スタックから一番上をだす。
      // fに時間を記載
      S.pop();
      color[u] = BLACK;
      f[u] = ++tt;

    }
 }
}


void dfs() {
  // 初期化
  for (int i = 0; i < n; i++) {
    color[i] = WHITE;
    nt[i] = 0;
  }
  tt = 0;

  // 未訪問のuを始点として深さ優先探索
  for (int u = 0; u < n; u++ ) {
    // 全頂点について、未訪問ならdfs_visit
    if ( color[u] == WHITE ) dfs_visit(u);
  }
  for (int i = 0; i < n; i++) {
    cout << i+1 << " " << d[i] << " " << f[i] << endl;
  }
}


int main() { 
  int u, k, v;
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++ ) M[i][j] = 0;
  }

  for (int i = 0; i < n; i++ ){
    cin >> u >> k;
    // 0オリジンに
    u--;
    for (int j = 0; j < k; j++) {
      cin >> v;
      // 0オリジンに
      v--;
      M[u][v] = 1;
    }
  }

  dfs();

  return 0;
}
