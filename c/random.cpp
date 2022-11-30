#include<iostream>
#include<cstdlib>      /* !!! */
#include<time.h>       /* !!! */

using namespace std;

int main() {
    char input;
	int num;
    srand(time(NULL));    /* !!! */
    
    while(true) {
    	cout<<"Premi INVIO per generare un numero casuale:";
    	input = getchar();
    	num = rand();
    	cout<<num<<endl;   	
    }
}

