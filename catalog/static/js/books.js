$("#selector").on("click",
    function () {
        let rightFlag = $(this).find("i").attr("class").includes('right')
        if (rightFlag) {
            $(".right #filter").css('display', "block")
            $(this).find("i").removeAttr("class").addClass("fas fa-caret-down fa-caret");
        } else {
            $(".right #filter").css('display', "none")
            $(this).find("i").removeAttr("class").addClass("fas fa-caret-right fa-caret");
        }
    }
)
