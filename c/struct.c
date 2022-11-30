#include <stdio.h>
#include <string.h>

struct Persona
{
    char nome[100];
    char cognome[100];
    /*
    char codice_fiscale[16];
    */
    int eta;
    int anno_n;
    char mese_n[10];
    int n_giorno_n;
} fillo;

int main()
{
    strcpy(fillo.nome, "Filippo");
    strcpy(fillo.cognome, "Ragni");
    /*
    char codice_fiscale = "";
    */
    fillo.eta = 16;
    fillo.anno_n = 2005;
    strcpy(fillo.mese_n, "aprile");
    fillo.n_giorno_n = 14;
    
    printf("%s %s e' nato il %d %s del %d e ha percio' %d anni d'eta'.", &fillo.nome, &fillo.cognome, fillo.n_giorno_n, &fillo.mese_n, fillo.anno_n, fillo.eta);

    return 0;
}
