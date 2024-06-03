#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i,j, count = 0, temp;
    scanf("%d", &n);
    int * arr = (int *)malloc(n * sizeof(int));
    for (i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }
    for(i=0;i<n;i++){
        for(j=i+1;j<n;j++){
            if((arr[i] - arr[j])/(i-j) == 1){
                count++;
            }
        }
    }
    
    printf("%d", count+count);
    
}