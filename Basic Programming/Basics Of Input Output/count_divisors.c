#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int l, r, k;
    int i;
    int count=0;
    scanf("%d %d %d", &l, &r, &k);
    
    for(i=l; i<=r; i++){
        if(i%k==0){
            count++;
        }
    }
    
    printf("%d", count);
}