// document.querySelectorAll('.book-btn').forEach(
//     element => {
//         element.addEventListener('click',(e)=>{
//             console.log(e.target)
//         })
//     }
// )

$(".book-btn").on("click",
    function () {
        $("#display-board").prepend(`<div>${$(this).attr('id')} <button class="cancel-btn">cancel</button></div>`);
        $(".cancel-btn").on("click",
            function () {
                $(this).parent().remove()
            }
        )
    }
)
