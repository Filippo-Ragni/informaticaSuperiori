#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//creo costanti di valore massimo inseribile e numero di valori nella lista
#define MAX_VAL 1000
#define VAL_MAX 1000000

//creo funzioni

//funzione per creare una lista contenente valori casuali
void crea_valori(int array[], int n_valori, int val_massimo)
{
    for (int i = 0; i < n_valori; i++)
    {
        array[i] = (rand() % val_massimo) + 1;
    }
}

//funzione per scambiare  valori all'interno della lista
void scambio(int *precedente, int *successivo)
{
	int temporaneo = *precedente;
	*precedente = *successivo;
	*successivo = temporaneo;
}

//funzione per il riordinamento della lista per selezione
void selezione(int lista[], int n)
{
int i, q, index, err = 1;
while(err!=0)
    {
    err = 0;
    for (int i = 0; i < (n - 1); i++)
        {
        index = i;
        for (int q = (i + 1); q < n; q++)
            {
            if(lista[index] > lista[q])
                {
                err+=1;
                scambio(&lista[index], &lista[q]);
                }
            }
        }
    }
}


//funzione bubble sort per il riordinamento della lista
void bubble_sort(int lista[], int n)
{
int i, j;
for (i = 0; i < n-1; i++)	

	for (j = 0; j < n-i-1; j++)
		if (lista[j] > lista[j+1])
			scambio(&lista[j], &lista[j+1]);
}

//funzione che restituisce i valori della lista
void print_lista(int lista[], int size)
{
	int i;
	for (i=0; i < size; i++)
		printf("%d; ", lista[i]);
	printf("\n");
}


int main()
{
    //creo la lista contenente valori casuali e ricavo il tempo impiegato per crearla per poi restituire il tutto
    clock_t iniziolista = clock();
    int lista[MAX_VAL];
    crea_valori(lista, MAX_VAL, VAL_MAX);
    clock_t finelista = clock();

    //creo una lista fantoccio identica alla precedente da riordinare col metodo bubble sort
    int lista_bubble[MAX_VAL];
    for (int i = 0; i < MAX_VAL; i++)
    {
        lista_bubble[i] = lista[i];
    }    
    
	int n = sizeof(lista)/sizeof(lista[0]);
    
/*
    printf("Valori della lista creata casualmente:\n\n");
	print_lista(lista, n);
    printf("\n");
    printf("Per creare una lista di valori casuali sono stati impiegati %f secondi.\n\n\n\n\n", 
    ((double)(finelista - iniziolista)) / CLOCKS_PER_SEC);
*/
    
    //riordinamento della lista col metodo per selezione 
    printf("Metodo per selezione:\n\n");
    int a = 0;
    while(a < MAX_VAL)
    {
        a+=100;
        clock_t inizioselezione = clock();
        selezione(lista, a);
        clock_t fineselezione = clock();
        printf("%d valori; %f secondi.\n",
        a, ((double)(fineselezione - inizioselezione)) / CLOCKS_PER_SEC);
/*
        if(a == MAX_VAL)
        {
            printf("\n\n%d valori della lista riordinata con bubble sort:\n\n", a);
        	print_lista(lista_bubble, a);
        }
*/
    }
    
    printf("\n\n\n");
    
    //riordinamento della lista fantoccio col metodo bubble sort
    printf("Metodo bubble sort:\n\n");
    int b = 0;
    while(b < MAX_VAL)
    {
        b+=100;
        clock_t iniziobubble = clock();
    	bubble_sort(lista_bubble, b);
        clock_t finebubble = clock();
        printf("%d valori; %f secondi.\n",
        b, ((double)(finebubble - iniziobubble)) / CLOCKS_PER_SEC);
/*
        if(b == MAX_VAL)
        {
            printf("\n\n%d valori della lista riordinata con bubble sort:\n\n", b);
        	print_lista(lista_bubble, b);
        }
*/
    }
    
    return 0;
}