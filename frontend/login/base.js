let element
$("#search-btn").on("click",
    () => {
        $("#search-box-moblie").toggleClass("clicked")
    }
)

$("#ham-btn").on("click",
    () => {
        $("#nav-item-moblie").toggleClass("clicked")
    }
)

$("#login").on("click",
    () => {
        $(".login-page").toggleClass("login-clicked")
    }
)

$(".login-layor").on("click",
    () => {
        $(".login-page").toggleClass("login-clicked")
    }
)