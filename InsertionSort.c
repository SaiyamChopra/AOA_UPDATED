#include <stdio.h>

void insertionSort(int arr[], int n) 
{
    void swap(int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    for (int i = 1; i < n; ++i) {
        int key = i;
        while (key > 0 && arr[key] < arr[key-1]) {
            swap(key-1, key);
            key--;
        }
    }
}

int main()
{
    int n;
    printf("Enter the size of list: ");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the elements: ");
    for (int x=0; x<n; x++){
        scanf("%d",&arr[x]);
    }
    insertionSort(arr, n);
    for (int i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}