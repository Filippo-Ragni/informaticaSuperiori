#include <stdio.h>

int main()
{
int i, n, m, c = 0;

printf("Quanti elementi vuoi inserire? \n");
scanf("%d",&n);

int a[n];

printf("Inserisci gli elementi: \n");

for (i=0;i<n;i++){
    scanf("%d",&a[i]);
    printf("\n");
}

int num, ind1, ind2;

for (i=1;i<n;i++){
    for (m=0;m<i;m++) {
        if (a[i] == a[m]) {
            num = a[i];
            ind1 = i;
            ind2 = m;
            c = 1;
        }
    }
}

int i1 = ind1 + 1, i2 = ind2 + 1;

if (c == 1) {
    printf("il numero %d è sia il %d°, che il %d° elemento dell'elenco.", num, i1, i2);
}

return 0;
}
