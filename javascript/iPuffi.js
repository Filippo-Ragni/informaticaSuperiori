let arrayOrari = [];
let listaColori = ["black", "red", "cyan", "orange", "purple"];

let addValue = () => {
    let newBody = document.body.innerHTML;
    let todayDate = new Date();
    let orarioAttuale = todayDate.toLocaleTimeString();
    arrayOrari.push(orarioAttuale);
    newBody += `<p id = "${arrayOrari.length-1}" color = "0"> sono le ${orarioAttuale} </p>`;
    document.body.innerHTML = newBody;
    document.getElementById(`${arrayOrari.length-1}`).style.color = "black";
}

let changeColor = () => {
    for (let i = 0; i < arrayOrari.length; i++){
        document.getElementById(`${i}`).style.color = listaColori[Number(`++${document.getElementById(${i}).color}`)];
    }
}