#include <stdio.h>
#include <stdlib.h>

int main() {
    int n,l,r, i, j, count = 0;
    scanf("%d %d %d", &n, &l, &r);
    int *arr = (int *)malloc(n * sizeof(int));
    for(i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }
    for(i=0;i<n;i++){
        for(j=i+1;j<n;j++){
            if( (arr[i]+arr[j]>=l && arr[i]+arr[j] <= r) && (arr[i] ^ arr[j]) & 1){
                count++;
            }
        }
    }
    printf("%d", count);
}