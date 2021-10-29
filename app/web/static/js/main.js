$('.dropdown-toggle').dropdown();
$('.carousel').carousel({
    interval: false
  });
$(document).ready( function() {
    var now = new Date();
    var today = now.getFullYear() + '-' + (now.getMonth() + 1) + '-' + now.getDate();
    $('#date').val(today);
});

function resetForm(formId) {
  document.getElementById(formId).reset();
};

(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();

function getUser(){
  var formElement = document.getElementById("userSearch");
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/get_userId");
  xhr.send(new FormData(formElement));
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var x=document.getElementById("userFoundContainer");
      if (x.style.display === "none") {
        x.style.display = "block";
      };
    };
    var xmlDoc = xml.responseXML;
    document.getElementById("userSearchedName").value = "preuba";
    var url = "/admin/users/"+ xmlDoc.getElementsByTagName("userId");
    document.getElementById("userSearchedURL").setAttribute("href", url);
  };
};
