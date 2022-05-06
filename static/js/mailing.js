var checkbox = document.querySelector("input[type=checkbox]");

checkbox.addEventListener('change', function() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/send', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send();
});