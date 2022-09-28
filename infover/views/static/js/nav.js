const burguer = document.getElementById("nav_icon_burger");
const xmark = document.getElementById("nav_icon_xmark");
const navMenu = document.querySelector(".nav__button_menu"); 
const nav = document.querySelector(".nav");
let screenWith = window.innerWidth; //obtiene el tamaño de la ventana.


xmark.classList.add("hidden");
xmark.addEventListener("click", () =>{
	visible_hidden();
});

burguer.addEventListener("click", () =>{
	visible_hidden();
});

function visible_hidden(){
	burguer.classList.toggle("hidden");
	xmark.classList.toggle("hidden");
	nav.classList.toggle("hidden");
}

function screenChanges(){
    screenWith = window.innerWidth;
    if (screenWith <=768){
    	nav.classList.add("hidden");
    	xmark.classList.add("hidden");
    	burguer.classList.remove("hidden");
    }else{
    	nav.classList.remove("hidden");
    }
}
window.onresize = function(){ //Se ejecuta cuando hay un cambio del tamaño.
	screenChanges();
};


screenChanges();