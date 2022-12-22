let coda = [];

const printLista = () => {
    let string = "";
    forEach ((e, i){
        string += `<li id = "${i}esimo"> ${e} <INPUT type = "button" value = "rimuovi" onclick = "delElement(document.getElementById("${i}esimo").value);"/></li>`;
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

const delElement = (identifier) => {
	coda.pop(document.getElementById(identifier).value);
	printLista();
}
