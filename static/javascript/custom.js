function goToHint(){
    window.alert("sometext");

    setTimeout(() => {  window.location.href = '/hint'; }, 1000);
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

 function updateUserStats(){
   $.ajax({
      url: "/update_user_stats",
      type: "POST",
      dataType: "json",
      success: function(data){
         $(dynamic_header).replaceWith(data)
      }
   })
}

function updateButton(){
   $.ajax({
      url: "/update_button",
      type: "POST",
      dataType: "json",
      success: function(data){
         $(update_button).replaceWith(data)
      }
   })
}
 
 function loadPlayer(_callback){
    $.ajax({
       url: "/load_player",
       type: "POST",
       dataType: "json",
       success: function(data){
          $(player_content).replaceWith(data)
       }
    });
 }
 
 function firstFunction(_callback){
    // do some asynchronous work
    // and when the asynchronous stuff is complete
    _callback();    
 }
 
 function secondFunction(){
    // call first function and pass in a callback function which
    // first function runs when it has completed
    firstFunction(function() {
        console.log('huzzah, I\'m done!');
    });    
 }