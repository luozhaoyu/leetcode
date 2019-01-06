#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define max( a, b ) ( ((a) > (b)) ? (a) : (b) )
struct node {
   struct node *left,*right;
   int val, val1;
};
typedef struct node node;
node * addElement(node * root, int x);
node * addRandomElement(node *, int, int);


/* Write your custom functions here */
int diameterOfTree(node * root) {
/* For your reference
  struct node {
   struct node *left,*right;
   int val;
};
*/
    int max_left, max_right;
    if (roor->left != NULL) {
        root.val = root
    }
    return root->left.val1 + root->right.val1;
}


int main(){
       
   node * root = NULL;
   int a[1000],K,i = 0,j = 0;
   int isBst = 0; scanf("%d",&isBst);    
   
   scanf("%d",&K);
   for( j = 0; j < K;j++ ) {
       scanf("%d",&a[i++]);    
   }

   for( i = 0; i < K;i++ ){
       if( !isBst ){            
           root = addRandomElement(root,a[i],i);
       } else {
           root = addElement(root,a[i]);
       }            
   }
   printf("%d",diameterOfTree(root));
   
return 0;
}
node * addElement(node * root, int x ){
   if( root == NULL ) {
       root = (node *) (malloc(sizeof(node))); 
       root->val = x;root->val1 = -1;
               root->left = NULL; root->right = NULL;
       return root;
   }
   if( x < root->val ) {
        root->left = addElement(root->left,x);
   }
   else {
       root->right = addElement(root->right,x);                            
   }
   return root;
}

node * addRandomElement(node *root, int x, int index){
   if( root == NULL ) {
       root = (node *) (malloc(sizeof(node))); 
       root->val = x;root->val1 = -1;
               root->left = NULL; root->right = NULL;
               return root;
   }

   if( index <=2 ){
       root->left = addRandomElement(root->left,x,index);
   } else {
       root->right = addRandomElement(root->right,x,index);
   }

   return root;
}
