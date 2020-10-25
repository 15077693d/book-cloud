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
