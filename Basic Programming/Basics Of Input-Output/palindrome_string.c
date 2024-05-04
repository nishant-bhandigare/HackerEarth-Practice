#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int i, j;
    int flag = 1;
    char string[100];
    scanf("%s", &string);
    
    for(i=0;i<(int)(strlen(string)/2);i++){
        if (string[i] != string[strlen(string) - 1 - i]){
            flag = 0;
            break;
        }
    }
    
    if (flag == 1){
        printf("YES");
    }else{
        printf("NO");
    }
}