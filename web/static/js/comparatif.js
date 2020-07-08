$('#pokemon-select-1').on('change', function (e) {
    var value = this.value;

    // Requete AJAX pour recuperer les donnees d'un pokemon
    $.ajax({
        url : '/pokemon/details/' + value,
        type : "POST",
        dataType : 'json',
        success : function(data) {
            $('#comparatif-1').append('<div class="text-center"><img src="https://pokeres.bastionbot.org/images/pokemon/' + data.id+ '.png" alt=""> </div><br>')
            $('#comparatif-1').append('<p><b>Nom : </b>' + data.name + ' </p>');
            $('#comparatif-1').append('<p><b>Poids : </b>' + data.weight + ' hectograms</p>');
            $('#comparatif-1').append('<p><b>Type : </b> <br>');
            data.types.forEach(element => $('#comparatif-1').append(element.type.name + ' <br>'));
            $('#comparatif-1').append('</p>');
            $('#comparatif-1').append('<p><b>Stats : </b> <br>');
            data.stats.forEach(function(item){
                $('#comparatif-1').append('<i>' + item.stat.name + '</i> : ')
                $('#comparatif-1').append(item.base_stat + ' <br>')
                
                
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
            $('#comparatif-2').append('<b>Nom : </b>' + data.name + ' <br>');
        },
        error : function() {
            console.log("ERREUR")
        }
    });

});