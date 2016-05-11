var cgi_heure = "/cgi-bin/ipi/heure_serveur.py"

function initialisations() {

    var d = new Date(); // Le jour
    var h = d.getHours(); // l'heure
    var m = d.getMinutes();
    var s = d.getSeconds();

    var heure_client = h + ":" + m + ":" + s;

    $('#heure').html(heure_client);
}

function demanderHeure() {
    
    var timezone = $("select[name='timezone']").val();

    $.ajax({
    
        url : cgi_heure,
        data : {"timezone" : timezone},
        beforeSend : function(){
            $('#heure').removeClass("well"); 
        },
        success : function(heure_serveur){
        
            console.log('Appel au script CGI réussi !!');
            $('#heure').html(heure_serveur).addClass("alert alert-success");
        }
    })
}

$('#demande_heure').click(function(){

    demanderHeure();

})


