#include<cstdio>  // 入出力ライブラリ
#include<cstdlib>  // いろんなユーティリティ提供
#include<string>  // 文字列ライブラリ
#include<iostream> // 入出力ライブラリ
using namespace std;  // 名前空間の面倒な修飾を省略できるstd::count がcountにここだと、Nodeの定義時に、structを書く必要がなくなる


struct Node {
  int key;  // int型のkey
  Node *right *left *parent;  # Node型へのポインタをright, left, parentは持つことができるという宣言
}


Node *root, *NIL;  // Node型へのrootポインタroot, NILの定義


void insert(int k){
  Node *y = NIL;
  Node *x = root;
  Node *z;

  z = (Node *)malloc(sizeof(Node));  // pointerに対してのメモリの動的な割り当て。zポインタからNodeのポインタへ渡してるっぽい.二重割り当てか?
  // 確保したメモリをNode型ポインタへキャスト。構造体のsizeofは構造体メンバのバイト数
  z->key = k;  // zオブジェクトのポインタに対して参照
  // zはNode型へのポインタ型変数。あるノードへのアドレスが入る
  // 上でzが指すNode用のメモリが確保
  // ここではzつまり確保したノードのアドレスのkeyがさすアドレスに変数を代入
  z->left = NIL;
  z->right = NIL;

  while (x != NIL) {
    y = x;
    if (z->key < x->key) {
      x = x->left;
    } else {
      x = x->right;
    }
  }
  z->parent = y
  while (x != NIL) {
    y = x;
    if (z->key < x->key) {
      x = x->left;
    } else {
      x = x->right;
    }
  }
  }
  z->parent = y
