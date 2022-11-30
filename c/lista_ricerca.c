#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//creo costanti di valore massimo inseribile e numero di valori nella lista
#define MAX_VAL 10000
int c;


//funzione per creare una lista contenente valori casuali
void crea_lista(int array[], int n_valori, int val_massimo)
{
    for (int i = 0; i < n_valori; i++)
    {
        array[i] = i+1;
    }
}

//funzione di ricerca sequenziale
int r_sequenziale(int v[], int n, int x) 
{ 
    int i; 
    for (i=0;i<n;i++){
        if(v[i]==x)
        {
            break;
        }
    }
    return(i==n) ? -1 : i;
}

//funzione di ricerca binaria
int r_binaria(int v[], int n, int i, int f) 
{ 
    int m= (i+f)/2; 
    c++;
    if (f<i) 
    { 
        return -1;
    } 
    if (v[m]>n) 
    { 
        return r_binaria(v,n,i,m-1);
    }
    else if (v[m]<n)
    {
        return r_binaria(v,n,m+1,f);
    }
    else
    {
        return m+1;
    }
}


int main()
{
    //creo la lista contenente valori casuali e ricavo il tempo impiegato per crearla per poi restituire il tutto
    int lista[MAX_VAL];
    crea_lista(lista, MAX_VAL, MAX_VAL);
    for (int i = 0; i < MAX_VAL; i++)
    {
        printf("%d ", lista[i]);
    }
    printf("\n\n");
	
	//chiedo un valore da cercare
	int ps, pb, x, val_s=0, val_b=0;
	
	//ricerca del numero richiesto per ricerca sequenziale
	printf("\nricerca sequenziale:\n");
	while(val_s<MAX_VAL)
	{
	    val_s+=1000;
	    x=(rand() % val_s) + 1;
	    
        clock_t start_s = clock();
        ps = r_sequenziale(lista, val_s, x);
        clock_t end_s = clock();
        printf("\nsecondi: %f", ((double)(end_s - start_s) / CLOCKS_PER_SEC));
        /*
        if (ps!=-1) 
        {
            printf("\nnumero: %d\nposizione: %d", x, ps+1); 
        }
        */
	}
    
    
    printf("\n\n");
    
    
    //ricerca del numero richiesto per ricerca binaria
	printf("\nricerca binaria:\n");
    while(val_b<MAX_VAL)
	{
	    val_b+=1000;
	    x=(rand() % val_b) + 1;
    	clock_t start_b = clock();
    	pb=r_binaria(lista,x,1,val_b);
    	clock_t end_b = clock();
        printf("\nsecondi:%f", ((double)(end_b - start_b) / CLOCKS_PER_SEC));
    	/*
        if (pb!=-1) 
        { 
            printf("\nnumero: %d\nposizione: %d", x, pb); 
            
        }
        */
	}
    
    return 0;
}