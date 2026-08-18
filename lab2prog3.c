#include <stdio.h>
#include <stdlib.h>
#include <time.h>


struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};

struct Node* createNode(int data) {
    struct Node* newNode =
        (struct Node*)malloc(sizeof(struct Node));

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


struct Node* search(struct Node* root, int key) {

    while (root != NULL) {

        if (key == root->data) {
            return root;
        }

        if (key < root->data) {
            root = root->left;
        }
        else {
            root = root->right;
        }
    }

    return NULL;
}


struct Node* findMin(struct Node* root) {

    while (root->left != NULL) {
        root = root->left;
    }

    return root;
}


struct Node* deleteNode(struct Node* root, int key) {

    if (root == NULL) {
        return NULL;
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

            root->right =
                deleteNode(root->right, temp->data);
        }
    }

    return root;
}

int height(struct Node* root) {

    if (root == NULL) {
        return 0;
    }

    int leftHeight = height(root->left);
    int rightHeight = height(root->right);

    return 1 + (leftHeight > rightHeight
                    ? leftHeight
                    : rightHeight);
}


void freeTree(struct Node* root) {

    if (root == NULL) {
        return;
    }

    freeTree(root->left);
    freeTree(root->right);

    free(root);
}


void shuffle(int arr[], int n) {

    for (int i = n - 1; i > 0; i--) {

        int j = rand() % (i + 1);

        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}



void runExperiment(int n, int type) {

    int *arr = (int*)malloc(n * sizeof(int));

   
    for (int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }

    
    if (type == 0) {
       
        shuffle(arr, n);
    }
    else if (type == 1) {
      
    }
    else {
        for (int i = 0; i < n / 2; i++) {
            int temp = arr[i];
            arr[i] = arr[n - 1 - i];
            arr[n - 1 - i] = temp;
        }
    }


    struct Node* root = NULL;

    clock_t start = clock();

    for (int i = 0; i < n; i++) {
        root = insert(root, arr[i]);
    }

    clock_t end = clock();

    double buildTime =
        (double)(end - start) / CLOCKS_PER_SEC;

    
    int treeHeight = height(root);


    start = clock();

    for (int i = 0; i < 1000; i++) {

        // Search for existing keys
        int key = arr[i % n];

        search(root, key);
    }

    end = clock();

    double searchTime =
        (double)(end - start) / CLOCKS_PER_SEC;


    start = clock();

    for (int i = 0; i < 500; i++) {

        int key = arr[i % n];

        root = deleteNode(root, key);
    }

    end = clock();

    double deleteTime =
        (double)(end - start) / CLOCKS_PER_SEC;


    printf("%-8d %-15s %-12.6f %-10d %-15.6f %-15.6f\n",
           n,
           type == 0 ? "Random" :
           type == 1 ? "Sorted" : "Reverse",
           buildTime,
           treeHeight,
           searchTime,
           deleteTime);

    freeTree(root);
    free(arr);
}


int main() {

    srand((unsigned int)time(NULL));

    printf("\nBST PERFORMANCE EXPERIMENT\n\n");

    printf("%-8s %-15s %-12s %-10s %-15s %-15s\n",
           "n",
           "Input",
           "Build(s)",
           "Height",
           "1000 Search(s)",
           "500 Delete(s)");

    printf("--------------------------------------------------------------------------\n");

    int sizes[] = {1000, 5000, 10000};

    for (int i = 0; i < 3; i++) {

        int n = sizes[i];

        runExperiment(n, 0);
        
        runExperiment(n, 1);

        runExperiment(n, 2);
    }

    return 0;
}