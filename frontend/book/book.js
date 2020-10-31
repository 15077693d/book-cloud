let element
$("#search-btn").on("click",
    () => {
        $("#search-box-moblie").toggleClass("clicked")
    }
)

$('[data-toggle="tooltip"]').tooltip();

$("#ham-btn").on("click",
    () => {
        $("#nav-item-moblie").toggleClass("clicked")
    }
)

$("#book-btn").on("click", function () {
    $(".overlay").css('display', "flex")
})

$(".overlay").on("click",
    function (event) {
        if (event.target.getAttribute("class") === "overlay") {
            $(this).hide()
        }
    }
)

// $(".book-pop-up").on("click",
//     function () {
//         $(this).css('display', "block")
//     })