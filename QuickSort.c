#include <stdio.h>

int partition(int arr[], int low, int high) {
    void swap(int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(i, j);
        }
    }
    
    swap(i + 1, high);  
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low <= high) {
        
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}



int main()
{
    int n;
    printf("Enter the size of list: ");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the elements: ");
    for (int x=0;x<n;x++)
    {
        scanf("%d",&arr[x]);
    }
    quickSort(arr, 0, n);
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    
    return 0;
}