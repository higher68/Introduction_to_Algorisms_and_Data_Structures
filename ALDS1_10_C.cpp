#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
static const int N = 1000;

int lcs(string X, string Y){
  int c[N+1][N+1];
  int m = X.size();
  int n = Y.size();
  int maxl = 0;
  X = ' ' + X;  // X[0]に空白を挿入
  Y = ' ' + Y;  // X[0]に空白を挿入
