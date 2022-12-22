let coda = [];

const addLast = () => {
    coda.push(document.getElementById("insertName").value);
    let string = "";
    for (e of coda){
        string += `<li> ${e} </li><INPUT type = "button" value = "rimuovi" onclick = "delElement();"/>`;
    }
    document.getElementById("list").innerHTML = string;
}