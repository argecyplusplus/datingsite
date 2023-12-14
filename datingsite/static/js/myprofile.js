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