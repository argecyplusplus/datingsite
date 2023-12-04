function selectAvatar() {
    document.getElementById("id_avatar").click();
};


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














/* document.getElementById("id_avatar").addEventListener("change",
  function() {
    var img = document.getElementById("avatar_img");
    var file = this.files[0];

    var reader = new FileReader();

    reader.onload = function(e) {
      img.src = e.target.result;
    };

    reader.readAsDataURL(file);
    }
  }); */

