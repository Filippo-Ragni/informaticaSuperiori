let coda = [];

const printLista = () => {
    let string = "";

// problema con la funzione printLista: l'argomento passato alla funzione delElement sarà sempre l'indice dell'ultimo elemento della lista
// ho pensato a mettere un id al tag <li>, ma come argomento a delElement dovrei passare comunque il getElementById col Number("${i}") come argomento, il ché non risolverebbe niente
    coda.forEach ((e, i) =>{
        string += `<li> 
        ${e} 
        <INPUT type = "button" value = "rimuovi" onclick = "delElement(${i});"/>
        </li>`;
    })
    document.getElementById("list").innerHTML = string;
}

const addLast = () => {
    coda.push(document.getElementById("insertName").value);
	printLista();
}

const delFirst = () => {
	document.getElementById("delName").value = coda.shift();
	printLista();
}

const delElement = (index) => {
	coda.pop(index);
	printLista();
}