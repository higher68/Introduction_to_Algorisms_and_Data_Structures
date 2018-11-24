#include <stdio.h>
#include <cstdio>    // 入出力ライブラリ
#include <cstdlib>   // いろんなユーティリティ提供
#include <iostream>  // 入出力ライブラリ
#include <string>    // 文字列ライブラリ
using namespace std;  // 名前空間の面倒な修飾を省略できるstd::count
                      // がcountにここだと、Nodeの定義時に、structを書く必要がなくなる

struct Node {
  int key;  // int型のkey
  Node *right, *left, *parent;
  // Node型へのポインタをright, left, parentは持つことができるという宣言
}

Node *root,
    *NIL;  // Node型へのrootポインタroot, NILの定義

void insert(int k) {
  Node *y = NIL;
  Node *x = root;
  Node *z;

  z = (Node *)malloc(sizeof(
      Node));  // pointerに対してのメモリの動的な割り当て。zポインタからNodeのポインタへ渡してるっぽい.二重割り当てか?
  // 確保したメモリをNode型ポインタへキャスト。構造体のsizeofは構造体メンバのバイト数
  z->key = k;  // zオブジェクトのポインタに対して参照
  // zはNode型へのポインタ型変数。あるノードへのアドレスが入る
  // 上でzが指すNode用のメモリが確保
  // ここではzつまり確保したノードのアドレスのkeyがさすアドレスに変数を代入
  z->left = NIL;
  z->right = NIL;
  // zに親の情報を入れ込む処理：yが親に相当
  while (x != NIL) {
    y = x;
    if (z->key < x->key) {
      x = x->left;
    } else {
      x = x->right;
    }
  }
  z->parent = y;
  // yに子の情報を入れる処理
  if (y == NIL) {
    root = z;
    if (z->key < y->key) {
      y->left = z;
    } else {
      y->right = z;
    }
  }
}

void inorder(Node *u) {
  if (u == NIL) return;
  inorder(u->left);
  printf(" %d", u->key);
  inorder(u->right);
}
void preorder(Node *u) {
  if (u == NIL) return;
  printf(" %d", u->key) i;
  prorder(u->left);
  prorder(u->right);
  
int main() {
  int n, i, x;
  string com;

  scanf("%d", &n);

  for (i = 0; i < n; i++) {
    cin >> com;  // stdio::cinは >>として、その先のstdinからの入力を入れれる
    if (com == "insert"){
      scanf("%d", &x);  // dだと10進数でxのアドレスに入力
      insert(x);
    } else if (com == "print" ) {
      inorder(root);
      printf("\n");
      preorder(root);
      printf("\n");
    }
  }
  
  return 0;  // 0を返すと正常終了。それ以外だと異常。
}
