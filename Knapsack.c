/*
     profits = {60, 100, 120, 150};
     weights = {10, 20, 30, 40};
     W = 50;
*/
#include <stdio.h>

// Function to find the maximum value in the knapsack
int knapsack(int profits[], int weights[], int N, int W) 
{
    int dp[N + 1][W + 1];
    // Step 2: Initialize DP Table
    for (int i = 0; i <= N; i++) {
        for (int j = 0; j <= W; j++) {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else if (weights[i - 1] <= j)
                dp[i][j] = (profits[i - 1] + dp[i - 1][j - weights[i - 1]] > dp[i - 1][j]) ?
                                                                                            profits[i - 1] + dp[i - 1][j - weights[i - 1]] 
                                                                                           : dp[i - 1][j];
            else
                dp[i][j] = dp[i - 1][j];
        }
    }
   // Step 4: Backtracking to Find Selected Items
    printf("Selected Items: ");
    int i = N, j = W;
    while (i > 0 && j > 0) 
    {
    // Check if item i was included by comparing with the value above
    if (dp[i][j] != dp[i - 1][j]) 
    {
        printf("%d ", i); // Print item number (1-based)
        j = j - weights[i - 1]; // Reduce remaining weight
    }
    i--; // Move to the previous item
    }
    printf("\n");
    return dp[N][W];
}

int main() {
    int N, W;
    printf("Enter number of items: ");
    scanf("%d", &N);

    int profits[N], weights[N];
    printf("Enter profits of items: ");
    for(int i = 0; i < N; i++){
        scanf("%d", &profits[i]);
    }
    printf("Enter weights of items: ");
    for(int i = 0; i < N; i++){
        scanf("%d", &weights[i]);
    }
    printf("Enter knapsack capacity: ");
    scanf("%d", &W);

    int max_value = knapsack(profits, weights, N, W);
    printf("Maximum Value = %d\n", max_value);

    return 0;
}
