#include <stdio.h>

int main()
{
int i, n, m, p;

printf("Quanti valori vuoi visualizzare? \n");
scanf("%d",&n);

int a[n];
a[0] = 1;
a[1] = 1;

for (i=2;i<n;i++){
    m = i - 1;
    p = i - 2;
    a[i] = (a[m] + a[p]);
}

printf("la serie è composta da: ");

for (i=0;i<n;i++){
    printf("%d ", a[i]);
}

return 0;
}
