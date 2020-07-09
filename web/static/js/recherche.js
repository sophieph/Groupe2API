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
            console.log("type : " + typeof(data));
            name = data.name;
            window.location.replace("/pokemon/" + name);
            if (empty(data)) {
                window.location.replace("/no_pokemon");
            }

        },
        error: function () {
            window.location.replace("/no_pokemon");
        }
    });

});