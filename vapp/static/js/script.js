$(document).ready(function(){
   $('#Username').change(function(){
     var Username = $(this).val();
    $.ajax({
        url : '/validate_Username/',
        data: {
            'Username':Username
        },
        dataType : 'json',
        succes : function(data) {
            if (data.is_taken){
                alert("username already exists");
            }
        }

    });

   });



});