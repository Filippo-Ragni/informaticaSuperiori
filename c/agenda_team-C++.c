/*programma svolto da Filippo Ragni, Alessandro Palbiani e Francesco Righetti;
Completare le modifiche verso C++ e implementare le funzioni 
di ricerca e ordinamento su chiave ID e Cognome. */


#include <iostream>
#include <string.h>


using namespace std;


#define N 6
#define MAXSTR 15


typedef struct {
        int id;
          string cognome;
        string nome;  
} s_arch;




s_arch archivio[N]={ 
        {1,"Rossi", "Mario"},
        {2,"Verdi", "Ugo"},
        {3,"Gagliardi", "Giovanni"},
        {4,"Plutone", "Pippo"},
};




void Visualizza(int pos)
{ 
int i=0;
while(i<pos)
{        
         cout << "\n      ID: " << archivio[i].id;
         cout << "\n COGNOME: " << archivio[i].cognome;
        cout << "\n    NOME: " << archivio[i].nome;


        i++;
 }
}


int Insert(int pos)
{


        if(pos>=N) {
                printf("\n\nHAI RAGGIUNTO IL LIMITE MASSIMO DI ELEMENTI");
                
        return(pos);
        }
        
        archivio[pos].id = pos+1;
        
        printf("\nNuovo Rcd n. %d:", pos+1);
        printf("\nCOGNOME:");
        cin >> archivio[pos].cognome;
        printf("   NOME:");
        cin >> archivio[pos].nome;


        pos++;
        return(pos);
}


void VisualizzaByCognome(int pos)
{ 
        char cognome[MAXSTR];
        int i=0, trovato=0;
        
        printf("\nQuale cognome cerchi?:");
         scanf("%s", cognome);
         
        for (i=0; i<pos; i++){
                 if(archivio[i].cognome == cognome) {
                 cout << "\n      ID: " << archivio[i].id;
                 cout << "\n COGNOME: " << archivio[i].cognome;
                cout << "\n    NOME: " << archivio[i].nome;
                         trovato=1;
                 }
         }
         if (trovato==0) 
                 printf("\nCOGNOME CERCATO NON PRESENTE");
}


void VisualizzaByID(int pos)
{ 
        int id[MAXSTR];
        int i=0, trovato=0;
        
        printf("\nQuale id cerchi?:");
         scanf("%d", id);
         
        for (i=0; i<pos; i++){
                 if(archivio[i].id == *id) {
                 cout << "\n      ID: " << archivio[i].id;
                 cout << "\n COGNOME: " << archivio[i].cognome;
                cout << "\n    NOME: " << archivio[i].nome;
                         trovato=1;
                 }
         }
         if (trovato==0) 
                 printf("\nID CERCATO NON PRESENTE");
}


void VisualizzaByNome(int pos)
{ 
        char nome[MAXSTR];
        int i=0, trovato=0;
        
        printf("\nQuale nome cerchi?:");
         scanf("%s", nome);
         
        for (i=0; i<pos; i++){
                 if(archivio[i].nome == nome) {
                 cout << "\n      ID: " << archivio[i].id;
                 cout << "\n COGNOME: " << archivio[i].cognome;
                cout << "\n    NOME: " << archivio[i].nome;
                         trovato=1;
                 }
         }
         if (trovato==0) 
                 printf("\nNOME CERCATO NON PRESENTE");
}


int menu_scelta(void)
{
  int selezione = 0;
  do
    {
    printf("\n" );
    printf("\n0 -> Esci");
    printf("\n1 -> Visualizza Archivio" );
    printf("\n2 -> Inserisci");
    printf("\n3 -> Ricerca per cognome");
    printf("\n4 -> Ricerca per ID");
    printf("\n5 -> Ricerca per nome");
    printf("\n" );
    printf("\nEffettua una scelta -> " );
    scanf("%d", &selezione );
    }
    while (selezione < 0 || selezione > 5);
  return selezione;
}


int main(void)
{
    int MyIndex=4; //indico il numero di elementi allocati nel vettore archivio
    int scelta;
    
    while((scelta=menu_scelta())!=0){
    switch(scelta){
        case 1: 
               Visualizza(MyIndex);
               break;
        case 2:
               MyIndex=Insert(MyIndex);
               break;
        case 3:
               VisualizzaByCognome(MyIndex);
               break;
        case 4:
               VisualizzaByID(MyIndex);
               break;
        case 5:
               VisualizzaByNome(MyIndex);
               break;
             }
    }             
    return 0;
}