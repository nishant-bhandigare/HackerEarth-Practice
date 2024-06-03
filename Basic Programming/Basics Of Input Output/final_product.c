#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    int n, i;
    long int answer = 1;
    scanf("%d", &n);
    int *arr = (int *)malloc(n*sizeof(int));
    
    for(i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }
    
    for(i=0;i<n;i++){
        answer = (answer * arr[i])%((int)pow(10,9) + 7);
    }
    
    printf("%d", answer);
    free(arr);
}