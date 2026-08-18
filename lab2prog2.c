#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};


struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;

    return newNode;
}

struct Node* insert(struct Node* root, int data) {
    if (root == NULL) {
        return createNode(data);
    }

    if (data < root->data) {
        root->left = insert(root->left, data);
    }
    else if (data > root->data) {
        root->right = insert(root->right, data);
    }

    return root;
}

void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

struct Node* findMin(struct Node* root) {
    struct Node* current = root;

    while (current != NULL && current->left != NULL) {
        current = current->left;
    }

    return current;
}


struct Node* deleteNode(struct Node* root, int key) {

   
    if (root == NULL) {
        return root;
    }


    if (key < root->data) {
        root->left = deleteNode(root->left, key);
    }

 
    else if (key > root->data) {
        root->right = deleteNode(root->right, key);
    }

    else {

       
        if (root->left == NULL && root->right == NULL) {
            free(root);
            return NULL;
        }

        else if (root->left == NULL) {
            struct Node* temp = root->right;
            free(root);
            return temp;
        }
   
        else if (root->right == NULL) {
            struct Node* temp = root->left;
            free(root);
            return temp;
        }

        else {
            
            struct Node* temp = findMin(root->right);

          
            root->data = temp->data;

            root->right = deleteNode(root->right, temp->data);
        }
    }

    return root;
}

int main() {

    struct Node* root = NULL;

    int keys[] = {50, 30, 70, 20, 40, 60, 80, 10};

    int n = sizeof(keys) / sizeof(keys[0]);

    for (int i = 0; i < n; i++) {
        root = insert(root, keys[i]);
    }

    printf("Original BST inorder: ");
    inorder(root);
    printf("\n\n");

    printf("Deleting leaf node 40...\n");

    root = deleteNode(root, 40);

    printf("Inorder after deleting 40: ");
    inorder(root);
    printf("\n\n");

    printf("Deleting node 20 (one child: 10)...\n");

    root = deleteNode(root, 20);

    printf("Inorder after deleting 20: ");
    inorder(root);
    printf("\n\n");

    printf("Deleting node 50 (two children: 30 and 70)...\n");

    root = deleteNode(root, 50);

    printf("Inorder after deleting 50: ");
    inorder(root);
    printf("\n");
    
    return 0;
}