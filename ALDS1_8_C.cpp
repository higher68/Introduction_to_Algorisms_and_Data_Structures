#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<iostream>
using namespace std;

struct Node {
  int key;
  Node *right, *left, *parent;
};

Node *root, *NIL;

Node * treeMinimum(Node *x) {
  while(x ->left != NIL) x = x->left;
  return x;
}



Node * find(Node *u, int k) {
  while (u != NIL && k != u->key) {
    if (k < u->key) u = u->left;
    else u = u->right;
  }
  return u;
}

Node * treeSuccessor (Node *x) {
  if (x->right != NIL) return treeMinimum(x->right);
  Node *y = x->parent;
  while( y != NIL && x == y->right ) {
    x = y;
    y = y->parent;
  }
  return y;
}

void treeDelete(Node *z){
  Node *y;  // 削除する対象
  Node *x;  // yの子
  // zは削除したいノード
  
  // 削除する節点を決める
  // zの子が一個以下のときzを削除。zに子がいない時はzを削除、子が1つでもそう 
  if (z->left == NIL || z->right == NIL)y = z;
  // zの子が二つの時は、zの次節点yのキーをzにコピー。yを消す
  else y = treeSuccessor(z);
  // yの子xを決める
  // yに左の子供がいる時
  if (y->left != NIL) {
    x = y->left;
  } else {
    // yに左の子供がいない時。右もいなかったら、NILになる。
    x = y->right;
  }
  // yに子供がいる時、yの親とxを繋ぐ
  if (x != NIL){
    x->parent = y->parent;
  }
  // yの親を決める
  if (y->parent == NIL ) {
    // 削除対象に親がいない時、削除したノードの子がrootになる
    root=x;
  } else {
    // 削除対象に親がいる時
    // 削除するノードが親の左の子のとき
    if (y == y->parent->left) {
      // 削除するノードの子を削除したノードの親の左の子供とする
      y->parent->left = x;
    } else {
      //　削除するノードが親の右の子のとき＼
      y->parent->right = x;
    }
  }
  // 削除したノードが、削除しようとしたノード出なかった時、つまり、削除しようとしたノードの左右に子供がいた時
  if (y != z) {
    // 削除したノードのキーをzのキーに
    z->key = y->key;
  }
  // 最後にyを削除
  free(y);
}

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
  } else {
    if (z->key < y->key) {
      y->left = z;
    } else {
      y->right = z;
    }
  }
  // 削除対象が、入れたものでない時、つまり、zに子供が存在する時
  if (y != z) {
   z->key = y->key;
  }
 free(y); 
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

  for (i = 0; i< n; i++) {
    cin >> com;
    if (com[0] == 'f' ){
      scanf("%d", &x);
      Node *t = find(root, x);
      if (t != NIL)printf("yes\n");
      else printf("no\n");
    } else if (com == "insert") {
      scanf("%d", &x);
      insert(x);
    } else if (com == "print") {
      inorder(root);
      printf("\n");
      preorder(root);
      printf("\n");
    } else if (com == "delete"){
      scanf("%d", &x);
      treeDelete(find(root, x));
    }
  }
}

