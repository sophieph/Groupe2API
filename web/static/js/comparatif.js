$('#pokemon-select-1').on('change', function (e) {
    var value = this.value;
    
    $.ajax({
        url : '/pokemon/details/' + value,
        type : "POST",
        dataType : 'json',
        success : function(data) {
                name = data.name
                console.log(name)
        },
        error : function() {
            console.log("ERREUR")
        }
    });

});