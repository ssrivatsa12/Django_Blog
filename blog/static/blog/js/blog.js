function openForm() {
document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}

function showDiv() {
  document.getElementById('post').style.display = "none";
  document.getElementById('loading').style.display = "block";
  setTimeout(function() {
    document.getElementById('loading').style.display = "none";
    document.getElementById('post').style.display = "block";
  },2000);
   
}



