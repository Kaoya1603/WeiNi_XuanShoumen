$( function() {
    $( "#autocomplete" ).autocomplete({
      source: contestNames
    });
  } );
//
//$('#autocomplete').on('change', function(){
//  var $this = $(this),
//      val = $this.val();
//    console.log($this);
//    console.log(val);
//    if (val in profiles)
//});