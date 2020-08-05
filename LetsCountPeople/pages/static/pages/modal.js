$(document).ready(() => {
  $('.add-gym').submit((e) => {
    e.preventDefault();
    console.log('모달 적용');
    const gymName = $(`input#${gym-name}[name=gym-name]`).val()
    const csrfmiddlewaretoken = e.data('csrfmiddlewaretoken')
    console.log(gymName);
    console.log(csrfmiddlewaretoken);
  })
})