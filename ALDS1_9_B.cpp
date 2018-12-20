#include<iostream>
using namespace std;
# define MAX 2000000

int H, A[MAX+1];

void maxHeapify(int i) {
  int l, r, largest;
  l = 2 * i;
  r = 2 * i + 1;

  // 左の子、自分、右の子で値が最大のノードを選ぶ
  // まずは左に関して、自分=iより大きいか判定
  if (l <= H && A[l] > A[i] ) largest = l;
  else largest = i;
  // 右に関して、一番大きいやつより大きいか判定
  if (r <= H && A[r] > A[largest]) largest = r;
  // 一番大きいのが自分でない時
  if (largest != i) {
    // swapは配列とかベクトルに格納されている値の交換
        swap(A[i], A[largest]);
        maxHeapify(largest);
  }
}

int main() {
  cin >> H;
  
  for (int i = 1;i <= H; i++) cin >> A[i];

  for (int i = H / 2; i >= 1; i--) maxHeapify(i);

  for (int i = 1; i <= H; i++) {
    cout << " " << A[i];
  }
  cout << endl;

  return 0;
}
