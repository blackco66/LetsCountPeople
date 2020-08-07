$('#login-form').submit((event) => {
  event.preventDefault();
  const request_path = $(event.currentTarget).data('next');

  $.ajax({
    url: '/accounts/login/?next{{request.path}}',
    method: 'POST',
    data: {
      login: $(`input#login-username`).val(),
      password: $(`input#password`).val(),
      csrfmiddlewaretoken: $(event.currentTarget).data('csrfmiddlewaretoken'),
      next: request_path,
    },
    dataType: 'json',
    success(res) {
      console.log(res);
      window.location.href = '/pages/';
    },
    error(response, status, error) {
      console.log(response, status, error);
      console.log(`/accounts/login/?next${request_path}`);
    },
  });
});
