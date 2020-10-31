$("#search-btn").on("click",
    () => {
        console.log("clicked serach")
        $("#search-box-moblie").toggleClass("clicked")
    }
)

$("#ham-btn").on("click",
    () => {
        $("#nav-item-moblie").toggleClass("clicked")
    }
)

$("#url").val(window.location.pathname)

$("#login").on("click",
    () => {
        console.log(123)
        $(".login-page").toggleClass("login-clicked")
        $('body').toggleClass("login-clicked-body")
    }
)

$("#login-moblie").on("click",
    () => {
        $(".login-page").toggleClass("login-clicked")
        $('body').toggleClass("login-clicked-body")
    }
)


$(".login-layor").on("click",
    () => {
        console.log(123)
        $(".login-page").toggleClass("login-clicked")
        $('body').toggleClass("login-clicked-body")
    }
)

$("#login-switch").on("click", function () {

})

$("#signup-switch").on("click", function () {
    console.log(123)
})


