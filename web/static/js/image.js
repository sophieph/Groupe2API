console.log('ok')

$('ul li').each(function(i)
{
    name_pokemon = $(this).attr('id'); // This is your rel value
    $.ajax({
        url : '/pokemon/image/' + name_pokemon,
        type : "POST",
        dataType : 'json',
        success : function(data) {
            console.log(data)
        },
        error : function() {
            console.log("ERREUR")
        }
    });

});