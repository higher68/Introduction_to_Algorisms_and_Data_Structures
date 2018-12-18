#include<iostream>
using namespace std;
#define MAX 100000  // defineは文字列を指定した文字で置き換える。constは変数を格納している。
// 2分接点の各情報を出力する
int parent(int i) { return i / 2;}
int left(int i) { return 2 * i;}
int right(int i) { return 2 * i + 1;}

int main() {
  int H, i, A[MAX+1];  // 1-オリジンのため +1する

  cin >> H;
  for (i =1; i <= H; i++) cin >> A[i];

  for (i = 1;i <= H; i++) {
    cout << "node " << i << ": key= " << A[i] << ", ";
    // <<はストリームへの入力
    if (parent(i) >= 1 ) cout << "parent key = " << A[parent(i)] << ", ";
    if (left(i) <= H ) cout << "left key = " << A[left(i)] << ", ";
    if (right(i) <= H ) cout << "right key = " << A[right(i)] << ", ";
    cout << endl;
  }
}

