let immages = [imm1.jpg, imm2.jpg, imm3.jpg];
let currentImg = document.getElementById("immID");

const ImmPrev = () => {
    let prevImm = 0;
    for (index in immages){
        if (currentImg.src == immages[i]){
            prevImm = i-=1;
        }
    }
    if (prevImm == -1){
        currentImg.src = immages[2];
    }
    else{
        currentImg.src = immages[prevImm];
    }
}

const ImmNext = () => {    
    let nextImm = 0;
    for (index in immages){
        if (currentImg.src == immages[i]){
            nextImm = i+=1;
        }
    }
    if (nextImm == 3){
        currentImg.src = immages[0];
    }
    else{
        currentImg.src = immages[nextImm];
    }
}