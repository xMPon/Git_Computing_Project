function myFunction() {
  var checkBox = document.getElementById("check");
  var changing = document.getElementById("time_to_change");
  if (checkBox.checked == true){
    changing.style.display = "block";
  } else {
     changing.style.display = "none";
  }
}
$(document).ready(function(){
    $('input:checkbox').click(function() {
        $('input:checkbox').not(this).prop('checked', false);
    });
});
//https://www.codexworld.com/how-to/allow-only-one-checkbox-to-be-checked-jquery/#:~:text=If%20you%20want%20to%20allow,first%2C%20include%20the%20jQuery%20library.&text=To%20modify%20the%20default%20functionality,user%20to%20select%20multiple%20checkboxes.