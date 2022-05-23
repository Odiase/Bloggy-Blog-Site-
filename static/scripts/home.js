const navbar = document.getElementById("navigation-tag");
const mobile_btn = document.getElementById("mobile-menu-btn");
const mobile_menu = document.querySelector(".mobile-menu");
const logo = document.querySelector(".tmp-blog-icon");
const search_btn = document.getElementById("search-wrapper-btn");
const search_field = document.getElementById("search-wrapper")
const close_search_btn = document.getElementById("close-search-field-btn");

const hidden_texts = document.querySelectorAll(".hide-vertical");
const intro_button = document.querySelector(".inner-header-text button");


// event listeners

/// header loading and menu functionality starts
if (hidden_texts){
    window.addEventListener("load", function(){
        for(let i = 0; i < hidden_texts.length; i++){
            console.log("starts")
            console.log(hidden_texts[i])
            hidden_texts[i].classList.add("show-vertical")
            console.log("finished")
        }
        if(intro_button) intro_button.classList.replace("hide-horizontal","show-horizontal");
        logo.classList.add("reveal-icon");
    })
}

window.addEventListener("scroll",function(){
    if (this.scrollY > 30){
        navbar.style.background = "rgb(10,100,10)"
    }
    else{
        navbar.style.background = "rgb(10,100,10)"
    }
})



mobile_btn.addEventListener("click",function(){
    if (mobile_menu.style.width == "60%"){
        mobile_menu.style.width = "0%"
    }
    else{
        mobile_menu.style.width = "60%"
    }
})

//search bar reveal and hide
search_btn.addEventListener("click",function(){
    search_field.style.top = "0"
})
close_search_btn.addEventListener("click",function(){
    search_field.style.top = "-100%"
})


// navabar scroll reveal functionality
let last_scrollTop = 0
function reveal_navbar(){
    if(window.scrollY > last_scrollTop){
        navbar.style.opacity = "0"
        last_scrollTop = window.pageYOffset
    }else{
        navbar.style.opacity = "1"
        last_scrollTop = window.scrollY
    }
}

window.addEventListener("scroll",reveal_navbar)
/// header loading and menu functionality ends