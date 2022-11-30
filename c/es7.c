#include <stdio.h>

int main()
{
int i, n, m=0, q=0, s;

printf("Di quale numero vuoi trovare i fattori primi? \n");
scanf("%d",&n);

int a[n];

for (i=2;i<n;i++){
    if ((n % i) == 0) {
        if (i == 2) {
        a[m] = i;
        m++;}
        else if (i != 2) {
            for (s=2;s<i;s++){
                if ((i % s) == 0) {
                    q = 1;
                }
            }
            if (q != 1) {
                a[m] = i;
                m++;
            }
        }
    }
    q = 0;
}

printf("il numero %d ha %d fattori, essi sono: ", n, m);
for (i=0;i<m;i++){
    printf("%d ", a[i]);
    }

return 0;
}
