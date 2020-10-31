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
        $(".login-page").toggleClass("login-clicked")
         $('body').toggleClass("login-clicked-body")
    }
)

$("#login-switch").on("click", function () {
    $(this).removeClass("btn-outline-primary").addClass("btn-primary");
    $("#signup-switch").removeClass("btn-primary").addClass("btn-outline-primary");
    $("#email").css("display","none")
    $("#user-confirm").attr("name","login")
})

$("#signup-switch").on("click", function () {
    $(this).removeClass("btn-outline-primary").addClass("btn-primary");
    $("#login-switch").removeClass("btn-primary").addClass("btn-outline-primary");
    $("#email").css("display","block")
    $("#user-confirm").attr("name","signup")
})

