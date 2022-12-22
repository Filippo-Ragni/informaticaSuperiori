let coda = [];

const printLista = () => {
    let string = "";
    for (e of coda){
        string += `<li> ${e} </li><INPUT type = "button" value = "rimuovi" onclick = "delElement();"/>`;
    }
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

const delElement = () => {
	
}
