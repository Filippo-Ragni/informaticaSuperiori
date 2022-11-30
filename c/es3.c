#include <stdio.h>

int main()
{

return 0;
}#include <stdio.h>

int main()
{
printf("inserisci numero n: ");
int n;
scanf("%d", &n);
printf("inserisci numero a: ");
int a;
scanf("%d", &a);
printf("inserisci numero b: ");
int b;
scanf("%d", &b);
if (n == a && n == b){
printf("sono tutti e tre uguali");
}
else if (n != a && n == b){
printf("n è ugual a b");
}
if (a == n && a != b){
printf("n è ugual ad a");
}
if (a != n && a == b){
printf("a è ugual a b");
}
if (b != n && b != a && n != a){
printf("sono tutti e 3 diversi");
}
return 0;
}