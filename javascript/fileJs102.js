let currentImg = 0;

const ImmPrev = () => {
    if (currentImg == 0){
        currentImg = 2;
    }
    else{
        currentImg -= 1;
    }
    document.getElementById("immID").src = "./imgGatti/imm" + currentImg + ".jpg";
}

const ImmNext = () => {
    if (currentImg == 2){
        currentImg = 0;
    }
    else{
        currentImg += 1;
    }
    document.getElementById("immID").src = "./imgGatti/imm" + currentImg + ".jpg";
}