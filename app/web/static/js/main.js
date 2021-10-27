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
}
function emailChange() {
  document.getElementById(email).value="{{request.form.email}}";
}
function phoneChange() {
  document.getElementById(phone).value="{{request.form.phone}}";
}

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