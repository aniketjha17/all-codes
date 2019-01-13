var l=document.querySelectorAll("li");
for (let i = 0; i < l.length; i++) {
    l[i].addEventListener("mouseover",function(){
        this.classList.add("a");
        this.classList.remove("b");
    });
    l[i].addEventListener("mouseout",function(){
        this.classList.add("b");
        this.classList.remove("a");
    });
    
}