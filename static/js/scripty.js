$(document).ready(function(){
    console.log("ok")

    $(document).on("submit", "#registrar-form", function(e){
        e.preventDefault()

        console.log("Si Entro")
        var form = $("#registrar-form").serialize()
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

    $(document).on("submit", "#ingresar-form", function(e){
        e.preventDefault()

        var form = $("#ingresar-form").serialize()
        $.ajax({
            url: "/postingresar",
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

    $(document).on("click", "#logout-link", function(e){
        e.preventDefault()

        $.ajax({
            url: "/logout",
            type: "GET",
            success: function(response){
                if (response=="OK"){
                    window.location.href = "/"
                }else{
                    alert("Ocurrió un error al intentar cerrar la sesión")
                }
            }
        });
    })

    $(document).on("submit", "#perfil-form", function(e){
        e.preventDefault()

        console.log("Es pagina")
        var form = $("#perfil-form").serialize()
        $.ajax({
            url: "/postPerfil",
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

    $(document).on("submit", "#crearnota-form", function(e){
        e.preventDefault()

        console.log("Si entro")
        var form = $("#crearnota-form").serialize()
        $.ajax({
            url: "/postcrearnoticia",
            type: "POST",
            data: form,
            success: function(response){
                console.log("antes json")
                result = JSON.parse(response.replace(/'/g, "\""))

                console.log("post json")
                console.log(result.resultado)
                if (result.resultado=="S"){
                    window.location.href = "/agregarimagennoticia"
                }else{
                    alert(result.descripcion)
                }
            }
        });
    });
});