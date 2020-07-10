let btnSubmit = $('#submit');


// Requete pour trouver un pokemon
btnSubmit.click(function (e) {
    let name_pokemon = $('#search').val();
    e.preventDefault();

    $.ajax({
        url: '/pokemon/details/' + name_pokemon,
        type: "POST",
        dataType: 'json',
        success: function (data) {
            
            if (data.name != undefined) {
                name = data.name;
                window.location.replace("/pokemon/" + name);
            } else {
                window.location.replace("/no_pokemon");
            }
        
        },
        error: function (e) {
            window.location.replace("/no_pokemon");
        }
    });

});