function add(a,b) {
    return a+b
}

// $(document).ready(function() {
//    $('#user-form-button').on('submit', function(event) {
//        $.ajax({
//            data : {
//                name : $("#user").val()
//            },
//            type : 'POST',
//            url : '/load_character'
//        })
//    });
// });

function speriamobene(){
   load_character();
   goToHint();
}

function load_character(){
   $.ajax({
      data : {
          name : $("#user").val()
      },
      type : 'POST',
      url : '/load_character'
  })
}

function goToHint(){
   window.location.href = '/hint';
}

function loadDecimal(){
    $.ajax({
       url: "/random_module",
       type: "POST",
       dataType: "json",
       success: function(data){
          $(random_update).replaceWith(data)
       }
    })
 }

 function loadCharacter(){
   $.ajax({
      url: "/load_character",
      type: "POST",
      dataType: "json",
      success: function(data){
         $(hint_content).replaceWith(data)
      }  
   })
}



function loadHint(){
   $.ajax({
      url: "/load_hint",
      type: "POST",
      dataType: "json",
      success: function(data){
         $(hint_content).replaceWith(data)
      }
   })
}

function loadCharacter2(){
   $.ajax({
      url: "/loading",
      type: "POST",
      dataType: "json",
      success: function(data){
         $(loading_icon).replaceWith(data)
      }
   })
}