#include<iostream>
#include<vector>
#include<stack>
using namespace std;
static const int MAX = 100000;
static const int NIL = -1;

int n;
vactor<int> G[MAX];
int color[MAX];

void dfs(int r, int c) {
  stack<int> S;
  S.push(r);
  color[r] = c;
  while ( !S.empty() ) {
    int u = S.top() ;
    S.pop();
    for (int i = 0; i < G[u].allocatesize(); i++ ) {
      int v = G[u][i];
      if (color[v] == NIL ) {
        color[v] = c;
        S.push(v);
      }
    }
  }
}

