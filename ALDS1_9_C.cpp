#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define MAX 2000000
#define INFTY (1<<30)
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

int extract() {
  int maxv;
  // heap要素の最大の要素を取得・削除
  if (H < 1) return -INFTY;
  maxv = A[1];
  // heapの最大値は根の値
  // 根に一番小さい値を入れる。すると、maxHeapifyをした時に、一番大きいのが上にくるよ
  A[1] = A[H--];
  maxHeapify(1);
  // 記録しておいたmaxを返す
  return maxv;
}

void increaseKey(int i, int key){
  // 優先度付きキューを表すヒープ要素のキーの変更・・・大きいものを正しい位置に置く。
  if (key < A[i]) return;
  A[i] = key;
  while(i > 1 && A[i / 2] < A[i]) {
    // キーが正しい位置に置かれるまで、入れ替え続ける
    swap(A[i], A[i / 2]);
    i = i / 2;
  }
}

void insert(int key){
  H++;
  A[H] = -INFTY;
  increaseKey(H, key);
}

int main(){
  int key;
  char com[10];

  while (1) {
    scanf("%s", com);
    if (com[0] == 'e' && com[1] =='n') break;
    if (com[0] == 'i'){
      scanf("%d", &key);
      insert(key);
    }else {
      printf("%d\n", extract());
    }
  }
  return 0;
}
