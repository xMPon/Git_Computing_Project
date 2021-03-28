function myFunction() {
  document.getElementById('time_to_change').style.display = "block";
  document.getElementById('updated_id').value = document.getElementById('check_id').innerText;
  document.getElementById('updated_description').value = document.getElementById('check_description').innerText;
  document.getElementById('updated_quantity').value = document.getElementById('check_quantity').innerText;
  document.getElementById('updated_price').value = document.getElementById('check_price').innerText;
}