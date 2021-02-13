$(document).ready(function(){
    console.log("ok")

    $(document).on("submit", "#contact-form", function(e){
        e.preventDefault()

        console.log("Si Entro")
        var form = $("#contact-form").serialize()
        console.log(form)
        $.ajax({
            url: "/postregister",
            type: "POST",
            data: form,
            success: function(response){
                result = JSON.parse(response.replace(/'/g, "\""))

                if (result.resultado=="S"){
                    window.location.href = "/"
                }else{
                    alert(result.descripcion)
                }
            }
        });
    });
});