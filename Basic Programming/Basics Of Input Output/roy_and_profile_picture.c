#include <stdio.h>
#include <stdlib.h>

int main() {
    int l, n, w, h;
    int i;
    scanf("%d", &l);
    scanf("%d", &n);
    
    for(i=0;i<n;i++){
        scanf("%d %d", &w, &h);
        if (w<l || h<l){
            printf("UPLOAD ANOTHER\n");
        }
        else{
            if(w==h){
                printf("ACCEPTED\n");
            }
            else{
                printf("CROP IT\n");
            }
        }
    }
}