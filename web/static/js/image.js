
// Affiche le nom du pokemon lorsqu'on passe la souris dessus
$('.pokemon').mouseover(function() {
    let name = $(this).attr('id');
    $('#name_pokemon').html(name);
});

// Creer une requete Ajax qui recupere le lien de l'image sur la liste des pokemon
$('ul li').each(function(i)
{
    name_pokemon = $(this).attr('id'); // This is your rel value

    $.ajax({
        url : '/pokemon/image/' + name_pokemon,
        type : "POST",
        dataType : 'json',
        success : function(data) {
                name = data.name
                $('.' + name).append('<img src="' + data.sprites.front_default + '" alt="Image ' + name + '">');
        },
        error : function() {
            console.log("ERREUR")
        }
    });

});