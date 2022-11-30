#include <stdio.h>

int main()
{
int i, n;
int m = 0;

printf("Quale numero vuoi verificare sia primo o meno? \n");
scanf("%d",&n);

for (i=2;i<n;i++){
    if ((n % i) == 0) {
        m = 1;
    }
}

if (m == 0) {
    printf("%d è un numero primo", n);
}

else {
    printf("%d non è un  numero primo", n);
}

return 0;
}
