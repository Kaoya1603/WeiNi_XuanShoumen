$(document).ready(function () {
    var comButton = $('.com-tab button');
    var modal = $('.modal');
    var modalCloseButton = $('.modal-close-button');

    modalCloseButton.on('click', toggleModal);

    comButton.on('click', toggleModal);

    function toggleModal() {
        modal.toggleClass('is-open');
    }
});

function addFavorite() {
    var text = $(event.target).text().slice(0, -1);
    var f = document.forms['add-fav'];

    if (f) {
        var comField = f.competition;

        if (comField) {
            comField.value = text;
        }
    }

//    var data = {
//      form: f,
//      com_name: text
//    };
//
//    var body = ['\r\n'];
//    for (var key in data) {
//      body.push('Content-Disposition: form-data; name="' + key + '"\r\n\r\n' + data[key] + '\r\n');
//    }
//
//    var xhr = new XMLHttpRequest();
//    xhr.open('POST', '/get_profile', true);
//
//    xhr.setRequestHeader('Content-Type', 'multipart/form-data;');
//
//    xhr.onreadystatechange = function() {
//      if (this.readyState != 4) return;
//
//      alert( this.responseText );
//    }
//    xhr.send(body);
};
