#include <stdio.h>

int main()
{
int n;
scanf("%d", &n);
int ris = 0;
for(int i=1; i<=n; i++){
    ris += i;
    printf("%d \n", ris);
}
printf("%d \n", ris);
return 0;
}