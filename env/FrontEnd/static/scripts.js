function myFunction() {
  var checkBox = document.getElementById("check");
  var time_to_change = document.getElementById("time_to_change");
      if (checkBox.checked == true){
      time_to_change.style.display = "block";
      } else {
         time_to_change.style.display = "none";
         }
}