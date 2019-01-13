var numSquare=6;
var colors=generateColors(numSquare);
var squares=document.querySelectorAll(".square");
var msg=document.querySelector("#message");
var newGame=document.querySelector("#newGame");
var easy=document.querySelector("#easy");
var hard=document.querySelector("#hard");
newGame.addEventListener("click",function(){
    colors=generateColors(numSquare);
    result=pickcolor();
    dis.textContent=result;
    msg.textContent = " ";
    this.textContent="New Color"
    for(var i=0;i<squares.length;i++){
        squares[i].style.background=colors[i];
    }
    
});
function pickcolor(){
   var r= Math.floor(Math.random() * colors.length);
   return colors[r];
}     
var result=pickcolor();
var dis=document.getElementById("col");
dis.style.color="white";
dis.textContent=result;
for(var i=0;i<squares.length;i++){
    squares[i].style.background=colors[i];
    squares[i].addEventListener("click",function(){
    var select=this.style.background;
    if(select === result){
        correctColor(select);
        msg.textContent="Correct";
        newGame.textContent = "Play Again?";
    }
    else{
        this.style.background="#232323";
        msg.textContent="Try Again";
    }
    });
}
function generateColors(num){
    var arr=[];
    for(var i=0;i<num;i++){
        arr.push(randomColors());
    }

    return arr;
}
function randomColors(){
    var r=Math.floor(Math.random()*256);
    var g=Math.floor(Math.random()*256);
    var b=Math.floor(Math.random()*256);
    return ("rgb("+r+", "+g+", "+b+")");
}
function correctColor(colors) {
    for(var i=0;i<squares.length;i++){
        squares[i].style.background=colors;
    }
}

easy.addEventListener("click",function(){
    numSquare = 3;
    easy.classList.add("selected");
    hard.classList.remove("selected");
    colors = generateColors(numSquare);
    result = pickcolor();
    dis.textContent = result;
    for(var i=0;i<squares.length;i++){
        if(colors[i]){
            squares[i].style.background=colors[i];
        }else{
            squares[i].style.display="none";
        }
    }

});
hard.addEventListener("click",function(){
    numSquare = 6;
    hard.classList.add("selected");
    easy.classList.remove("selected");
    colors = generateColors(numSquare);
    result = pickcolor();
    dis.textContent = result;
    for (var i = 0; i < squares.length; i++) {
        
        squares[i].style.background = colors[i];
        squares[i].style.display = "block";
    }
});