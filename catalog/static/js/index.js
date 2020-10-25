$('.overlay').on("click",
    (e) => {
        $(".card-expand").css("display", "none")
        $(".overlay").css("display", "none")
    }
)

$('.card-container').on("click",
    function () {
        $(this).find(".card-expand").css("display", "block")
        $(".overlay").css("display", "block")
    }
)

$('.container').on("click", '.card-container',
    function () {
        const columnNum = $('.container').css('grid-template-columns').split(" ").length
        const i = $(this).index()
        switch (columnNum) {
            case 2:
                if (i%2===0){
                    $('.card-expand').css("right",0)
                    $('.card-expand').css("left","")
                }else{
                    $('.card-expand').css("left",0)
                    $('.card-expand').css("right","")
                }
                break;
            case 3:
                if ([1,4,7,10].includes(i)){
                 $('.card-expand').css("left",0)
                    $('.card-expand').css("right","")
                }else{
                     $('.card-expand').css("right",0)
                    $('.card-expand').css("left","")
                }
                break;
            default:
                break;
        }
    }
)

