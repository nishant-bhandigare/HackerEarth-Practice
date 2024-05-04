#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i;
    long int product = 1; 
    scanf("%d", &n);
    
    for(i=1;i<=n;i++){
        product = product * i;
    }
    
    printf("%d", product);
}