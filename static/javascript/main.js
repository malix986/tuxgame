function add(a,b) {
    return a+b
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
         $(loading_button).replaceWith(data)
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