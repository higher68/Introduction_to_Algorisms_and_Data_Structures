#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<iostream>
using namespace std;


struct Node {
  int key;
  Node *right, *left, *parent;
}

Node *root, *NIL;

Node * treeminimum(Node *x) {
  while(x ->left != NIL) x = x->keyleft;
  return x;
}



Node *find(Node *u, int k) {
  while (u != NIL && k != u->key) {
    if (k < u->key) u = u-left;
    else u = u->left;
  }
  return u;
}

Node * treeSuccessor (Node *x) {
  if (x->right != NIL) return treeminimum;


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
    } else if (com == "print") {
      inorder(root);
      printf("\n");
      preorder(root);


