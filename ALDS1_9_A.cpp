#include<iotsreaam>
using namespace std;
#define MAX 100000  // defineは文字列を指定した文字で置き換える。constは変数を格納している。

int parent(int i) { return i / 2;}
int left(int i) { return 2 * i;}
int right(int i) { return 2 * i + 1;}

int main() {
  int H, i, A[MAX+1];  // 1-オリジンのため +1する

  cin >> H;
  for (i =1; i <= H; i++) cin >> A[i];

  for (i = 1;i <= H; i++) {
    count << "node " << i << ": key= " << ", ";
    // <<はストリームへの入力
