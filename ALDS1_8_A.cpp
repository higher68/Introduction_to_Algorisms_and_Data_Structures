#include <cstdio>    // 入出力ライブラリ
#include <cstdlib>   // いろんなユーティリティ提供
#include <string>    // 文字列ライブラリ  
#include <iostream>  // 入出力ライブラリ
using namespace std;  // 名前空間の面倒な修飾を省略できるstd::count
                      // がcountにここだと、Nodeの定義時に、structを書く必要がなくなる

struct Node {
  int key;  // int型のkey
  Node *right, *left, *parent;
  // Node型へのポインタをright, left, parentは持つことができるという宣言
};  // struceの定義のあとは、セミコロンいる

Node *root, *NIL;  // Node型へのrootポインタroot, NILの定義

void insert(int k) {
  // cout << "\ngeho";
  // exit(0);
  Node *y = NIL;
  Node *x = root;
  Node *z;
  // cout << "\nhge";
  // exit(0); 
  z = (Node *)malloc(sizeof(Node));  // pointerに対してのメモリの動的な割り当て。zポインタからNodeのポインタへ渡してるっぽい.二重割り当てか?
  // 確保したメモリをNode型ポインタへキャスト。構造体のsizeofは構造体メンバのバイト数
  // cout << "\nheeeege";
  // exit(0); 
  z->key = k;  // zオブジェクトのポインタに対して参照
  // zはNode型へのポインタ型変数。あるノードへのアドレスが入る
  // 上でzが指すNode用のメモリが確保
  // ここではzつまり確保したノードのアドレスのkeyがさすアドレスに変数を代入
  z->left = NIL;
  z->right = NIL;
  // zに親の情報を入れ込む処理：yが親に相当
  // cout << "\nheeeege";
  // printf("\nhogeyasu"); 
  // printf("\nhogeyasu3333333333333333"); 
  // cout << "\n";
  // cout << x;
  // cout << "\n";
  // cout << NIL;
  // if ( x == NIL){
    // cout << "\nyes";
  // }
  // exit(0);
  while (x != NIL) {
    // cout << "\nstart hoge";
    y = x;
    if (z->key < x->key) {
      x = x->left;
    } else {
      x = x->right;
    }
  }
  // cout << "hoge1\n";
  z->parent = y;
  // yに子の情報を入れる処理
  // exit(0); 
  // cout << y; 
  // cout << "\n";
  // cout << NIL;
  // cout << "hoge2\n";
  if (y == NIL) {
    // cout << "hoge3\n";
    root = z;
    // cout << "hoge4\n";
    // cout << z->key;
    // cout << "hoge5\n";
  } else {
    // cout << y->key;
    // cout << "hoge6\n";
    // cout << z->key;
    if (z->key < y->key) {
      y->left = z;
    } else {
      y->right = z;
    }
    // cout << "hoge5\n";
  }
  // printf("\nhoge2");
}

void inorder(Node *u) {
  if (u == NIL) return;
  inorder(u->left);
  printf(" %d", u->key);
  inorder(u->right);
}
void preorder(Node *u) {
  if (u == NIL) return;
  printf(" %d", u->key);
  preorder(u->left);
  preorder(u->right);
}  
int main() {
  int n, i, x;
  string com;

  scanf("%d", &n);
  // printf("%d", n);
  // exit(0);
  for (i = 0; i < n; i++) {
    // printf("hogehoge");
    cin >> com;  // stdio::cinは >>として、その先のstdinからの入力を入れれる
    // scanf("%d", &x);  // dだと10進数でxのアドレスに入力
    // cout << com;
    // cout << x;
    // exit(0);
    // printf("hohoho");
    if (com == "insert"){
      // cout << com;
      // exit(0); 
      scanf("%d", &x);  // dだと10進数でxのアドレスに入力
      // cout << com;
      // cout << x;
      // cout << "hoge";
      // exit(0); 
      insert(x);
      // printf("hoge");
    } else if (com == "print" ) {
      inorder(root);
      printf("\n");
      preorder(root);
      printf("\n");
    }
  }
  
  return 0;  // 0を返すと正常終了。それ以外だと異常。
}
