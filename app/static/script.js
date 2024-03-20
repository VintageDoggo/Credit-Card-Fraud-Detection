$("#form1").submit(function(){
    e.preventDefault();
    console.log(5555)

    $.ajax({
        method: "POST",
        url: "/predict",
        data: { name: "John", location: "Boston" }
      }).done(function( msg ) {
          alert( "Data Saved: " + msg );
        });
  });
