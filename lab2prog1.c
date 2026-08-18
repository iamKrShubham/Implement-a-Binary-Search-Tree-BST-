# include <stdio.h>
# include <stdlib.h>
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


void preorder(struct Node* root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }

    }

void postorder(struct Node* root) {
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}

struct Node* search(struct Node* root, int key) {

    if (root == NULL) {
        return NULL;
    }

    if (root->data == key) {
        return root;
    }

    if (key < root->data) {
        return search(root->left, key);
    }

    return search(root->right, key);
}

void checkSorted(struct Node* root, int* previous, int* sorted) {
    if (root == NULL) {
        return;
    }

    checkSorted(root->left, previous, sorted);

    if (*previous != -1 && root->data <= *previous) {
        *sorted = 0;
    }

    *previous = root->data;
    checkSorted(root->right, previous, sorted);
}

int main() {

    struct Node* root = NULL;

    int keys[] = {50, 30, 70, 20, 40, 60, 80, 10};

    int n = sizeof(keys) / sizeof(keys[0]);

    
    for (int i = 0; i < n; i++) {
        root = insert(root, keys[i]);
    }

    printf("Inorder Traversal: ");
    inorder(root);
    printf("\n");

    printf("Preorder Traversal: ");
     preorder(root);
    printf("\n");

    printf("Postorder Traversal: ");
    postorder(root);
    printf("\n");

    int previous = -1;
    int sorted = 1;

    checkSorted(root, &previous, &sorted);

    if (sorted) {
        printf("Verification: Inorder traversal is in sorted order.\n");
    } else {
        printf("Verification: Inorder traversal is NOT in sorted order.\n");
    }

    int key1 = 40;

    if (search(root, key1) != NULL) {
        printf("Search %d: Key found in the BST.\n", key1);
    } else {
        printf("Search %d: Key not found in the BST.\n", key1);
    }

    int key2 = 90;

    if (search(root, key2) != NULL) {
        printf("Search %d: Key found in the BST.\n", key2);
    } else {
        printf("Search %d: Key not found in the BST.\n", key2);
    }

    return 0;
}