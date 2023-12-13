function selectAvatar() {
  var input = document.getElementById("id_avatar");
  input.click();
  input.onchange = function () {
    var reader = new FileReader();
    reader.onload = function(e) {
      var img = document.getElementById("user_avatar");
      img.src = e.target.result;
    };
    reader.readAsDataURL(input.files[0]);
  };
};

function validateForm() {
  var minv = document.getElementById('min').value;
  var maxv = document.getElementById('max').value;

  // Проверить значения полей формы
  if (minv > maxv) {
    alert('Введите имя');
    return false; // предотвратить отправку формы
  }

  return true; // разрешить отправку формы, если все значения проходят проверку
}

var form = document.getElementById('myForm');

form.addEventListener('submit', function(event) {
  // Отменить отправку формы по умолчанию
  event.preventDefault();

  // Запустить функцию проверки значений
  var isValid = validateForm();

  if (isValid) {
    // Если значения проходят проверку, можно отправить форму
    form.submit();
  }
});