function selectAvatar() {
  let input = document.getElementById("id_avatar");
  input.click();
  input.onchange = function () {
    let reader = new FileReader();
    reader.onload = function(e) {
      let img = document.getElementById("user_avatar");
      img.src = e.target.result;
    };
    reader.readAsDataURL(input.files[0]);
  };
};

function ChangeLabel(value) {
  len = value.length;
  var label = document.querySelector("label[for='id_description']");
  label.innerHTML = "О себе: " + value.length + "/300";
}

document.addEventListener("DOMContentLoaded", function() {
  let textarea = document.getElementById("id_description");
  textarea.style.height = 'auto';
  textarea.style.height = (textarea.scrollHeight) + 'px';
})

function autoResizeTextarea(element) {
  element.style.height = 'auto';
  element.style.height = (element.scrollHeight) + 'px';
}

function validateForm(event) {
  let min_value = parseInt(document.getElementById("minV").value);
  let max_value = parseInt(document.getElementById("maxV").value);

  if (min_value > max_value) {
    alert("Исправьте возраст!");
    event.preventDefault();
  }
}


// function validateForm() {
//   var minv = document.getElementById('min').value;
//   var maxv = document.getElementById('max').value;

//   // Проверить значения полей формы
//   if (minv > maxv) {
//     alert('Введите имя');
//     return false; // предотвратить отправку формы
//   }

//   return true; // разрешить отправку формы, если все значения проходят проверку
// }

// var form = document.getElementById('myForm');

// form.addEventListener('submit', function(event) {
//   // Отменить отправку формы по умолчанию
//   event.preventDefault();

//   // Запустить функцию проверки значений
//   var isValid = validateForm();

//   if (isValid) {
//     // Если значения проходят проверку, можно отправить форму
//     form.submit();
//   }
// });