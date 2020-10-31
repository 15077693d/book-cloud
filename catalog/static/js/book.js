$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

$("#book-btn").on("click", function () {
    $(".book-overlay").css('display', "flex")
})

$(".book-overlay").on("click",
    function (event) {
    console.log(event.target.getAttribute("class"))
        if (event.target.getAttribute("class") === "book-overlay") {
            $(this).hide()
        }
    }
)