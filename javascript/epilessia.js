//versione epilettica

let trafficLight = () => {
    setTimeout(() => {
    setInterval (
        () => {
            document.body.innerHTML="";
            document.body.style.backgroundColor = "red";
        }
        , 3);

    setTimeout(() => {
        setInterval (
            () => {
                document.body.style.backgroundColor = "yellow";
            }
            , 3);

        setTimeout(() => {
            setInterval (
                () => {
                    document.body.style.backgroundColor = "green";
                }
                , 3);
        }, 1);
    }, 1);
    }, 1000);
}

/*

//versione non epilettica

let trafficLight = () => {
    setInterval (
        () => {
            document.body.innerHTML="";
            document.body.style.backgroundColor = "yellow";
        }
        , 10000);

    setTimeout(() => {
        setInterval (
            () => {
                document.body.style.backgroundColor = "red";
            }
            , 10000);

        setTimeout(() => {
            setInterval (
                () => {
                    document.body.style.backgroundColor = "green";
                }
                , 10000);
        }, 4000);
    }, 2000);
}
*/