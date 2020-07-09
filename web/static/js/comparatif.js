$('#pokemon-select-1').on('change', function (e) {
    var value = this.value;

    // Requete AJAX pour recuperer les donnees d'un pokemon
    $.ajax({
        url : '/pokemon/details/' + value,
        type : "POST",
        dataType : 'json',
        success : function(data) {
            $('#comparatif-1').empty();
            $('#comparatif-1').append('<div class="text-center"><img src="https://pokeres.bastionbot.org/images/pokemon/' + data.id+ '.png" alt=""> </div><br>')
            $('#comparatif-1').append('<p><b>Nom : </b>' + data.name + ' </p>');
            $('#comparatif-1').append('<p><b>Poids : </b>' + data.weight + ' hectograms</p>');
            $('#comparatif-1').append('<p><b>Type : </b> <br>');
            data.types.forEach(element => $('#comparatif-1').append(element.type.name + ' <br>'));
            $('#comparatif-1').append('</p>');
            $('#comparatif-1').append('<p><b>Stats : </b> <br>');
            data.stats.forEach(function(item){
                $('#comparatif-1').append('<i>' + item.stat.name + '</i> : ')
                $('#comparatif-1').append('<span class="' + item.stat.name + '-1">' +item.base_stat + '</span> <br>')
              });
            $('#comparatif-1').append('</p>');
        
        },
        error : function() {
            console.log("ERREUR")
        }
    });


});

$('#pokemon-select-2').on('change', function (e) {
    var value = this.value;

    // Requete AJAX pour recuperer les donnees d'un pokemon
    $.ajax({
        url : '/pokemon/details/' + value,
        type : "POST",
        dataType : 'json',
        success : function(data) {
            $('#comparatif-2').empty();
            $('#comparatif-2').append('<div class="text-center"><img src="https://pokeres.bastionbot.org/images/pokemon/' + data.id+ '.png" alt=""> </div><br>')
            $('#comparatif-2').append('<p><b>Nom : </b>' + data.name + ' </p>');
            $('#comparatif-2').append('<p><b>Poids : </b>' + data.weight + ' hectograms</p>');
            $('#comparatif-2').append('<p><b>Type : </b> <br>');
            data.types.forEach(element => $('#comparatif-2').append(element.type.name + ' <br>'));
            $('#comparatif-2').append('</p>');
            $('#comparatif-2').append('<p><b>Stats : </b> <br>');
            data.stats.forEach(function(item){
                $('#comparatif-2').append('<i>' + item.stat.name + '</i> : ')
                $('#comparatif-2').append('<span class="' + item.stat.name + '-2">' +item.base_stat + '</span> <br>')
              });
            $('#comparatif-2').append('</p>');        
        },
        error : function() {
            console.log("ERREUR")
        }
    });

});

// Compare les stats en utilisant des couleurs
$('.comparatif').mouseover( function() {
    
    let hp1 = parseInt($('.hp-1').text());
    let hp2 = parseInt($('.hp-2').text());
    let attack1 = parseInt($('.attack-1').text());
    let attack2 = parseInt($('.attack-2').text());
    let defense1 = parseInt($('.defense-1').text());
    let defense2 = parseInt($('.defense-2').text());
    let special_attack1 = parseInt($('.special-attack-1').text());
    let special_attack2 = parseInt($('.special-attack-2').text());
    let special_defense1 = parseInt($('.special-defense-1').text());
    let special_defense2 = parseInt($('.special-defense-2').text());
    let speed1 = parseInt($('.speed-1').text());
    let speed2 = parseInt($('.speed-2').text());


    if (hp1 > hp2) {
        $('.hp-1').css("color", "green");
        $('.hp-1').css("font-weight", "bold");
        $('.hp-2').css("color", "red");
    } else if (hp2 > hp1) {
        $('.hp-2').css("color","green");
        $('.hp-2').css("font-weight", "bold");
        $('.hp-1').css("color", "red");
    }

    if (attack1 > attack2) {
        $('.attack-1').css("color", "green");
        $('.attack-1').css("font-weight", "bold");
        $('.attack-2').css("color", "red");
    } else if (attack2 > attack1) {
        $('.attack-2').css("color","green");
        $('.attack-2').css("font-weight", "bold");
        $('.attack-1').css("color", "red");
    }

    if (defense1 > defense2) {
        $('.defense-1').css("color", "green");
        $('.defense-1').css("font-weight", "bold");
        $('.defense-2').css("color", "red");
    } else if (defense2 > defense1) {
        $('.defense-2').css("color","green");
        $('.defense-2').css("font-weight", "bold");
        $('.defense-1').css("color", "red");
    }

    if (special_attack1 > special_attack2) {
        $('.special-attack-1').css("color", "green");
        $('.special-attack-1').css("font-weight", "bold");
        $('.special-attack-2').css("color", "red");
    } else if (special_attack2 > special_attack1) {
        $('.special-attack-2').css("color","green");
        $('.special-attack-2').css("font-weight", "bold");
        $('.special-attack-1').css("color", "red");
    }

    if (special_defense1 > special_defense2) {
        $('.special-defense-1').css("color", "green");
        $('.special-defense-1').css("font-weight", "bold");
        $('.special-defense-2').css("color", "red");
    } else if (special_defense2 > special_defense1) {
        $('.special-defense-2').css("color","green");
        $('.special-defense-2').css("font-weight", "bold");
        $('.special-defense-1').css("color", "red");
    }


    if (speed1 > speed2) {
        $('.speed-1').css("color", "green");
        $('.speed-1').css("font-weight", "bold");
        $('.speed-2').css("color", "red");
    } else if (speed2 > speed1) {
        $('.speed-2').css("color","green");
        $('.speed-2').css("font-weight", "bold");
        $('.speed-1').css("color", "red");
    }

});


