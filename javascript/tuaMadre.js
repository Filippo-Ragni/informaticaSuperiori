let coda = [];

const printLista = () => {
    let string = "";

    coda.forEach ((e, i) =>{
        string += `<li> 
        ${e}
        <INPUT type = "button" value = "rimuovi" onclick = "delElement(${i});">
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
    delete coda[index];
    printLista();
}