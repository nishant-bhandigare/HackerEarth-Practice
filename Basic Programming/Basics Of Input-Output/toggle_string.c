#include <stdio.h>
#include <string.h>

int main() {
    int i;
    int diff  = 32;
    char string[100];
    scanf("%s", &string);
    
    for (i=0;i<strlen(string);i++){
        if (string[i]>=65 && string[i]<=90)
            string[i] = string[i] + diff;
        else if (string[i]>=97 && string[i]<=122)
            string[i] = string[i] - diff;
    }
    
    printf("%s", string);
}