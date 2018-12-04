#include<iostream>
using namespace std;
# define MAX 2000000

int H, A[MAX+1];

void maxHeapify(int i) {
  int l, r, largest;
  l = 2 * i;
  r = 2 * i + 1;

  // 左の子、自分、右の子で値が最大のノードを選ぶ
  if (l <= H && A[r] > A[largest] ) largest = r;
  else largest = i;
  if (r <= H && A[largest]) larest = r;

  if (largest != i) {
        swqp(A[i], A[largest]);
        maxHeapify(largest);
  }
}

int main() {
  cin >> H;
  
  for (int i = 1;i <= H: i++) cin >>A[i];

  for (int i = H / 2; i >= 1; i--) maxHeapify(i);

  for (int i = 1; i <= H; i++) {
    count << " " << A[i]
  }
  count << endl;

  return 0;
}
