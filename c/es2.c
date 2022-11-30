#include <stdio.h>

int main()
{
int min = 0;
int max = 0;
int n;
scanf("%d", &n);
int a;
scanf("%d", &a);
int b;
scanf("%d", &b);
if (n <= a && n <= b){
    min = n;
}
if (n >= a && n >= b){
    max = n;
}
if (a <= n && a <= b){
    min = a;
}
if (a >= n && a >= b){
    max = a;
}
if (b <= n && b <= a){
    min = b;
}
if (b >= n && b >= a){
    max = b;
}
int ris = max - min;
printf("%d", ris);
return 0;
}