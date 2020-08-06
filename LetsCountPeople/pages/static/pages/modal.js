$(document).ready(() => {
  $('.add-gym').submit((e) => {
    e.preventDefault();

    $.ajax({
      type: 'POST',
      url: `/pages/add-gym/`,
      data: {
        csrfmiddlewaretoken: $(e.currentTarget).data('csrfmiddlewaretoken'),
        name: $(`input#gym-name`).val(),
        address: $(`input#gym-address`).val(),
        latitude: '',
        longitude: ''
      },
      dataType: 'json',
      success: function(response) {
        console.log('성공');
        window.location.href = '/pages/';
      },
      error: function(response, status, error) {
        console.log('실패');
      },
      complete: function(response) {
        console.log('완료');
      }
    })
  })
})