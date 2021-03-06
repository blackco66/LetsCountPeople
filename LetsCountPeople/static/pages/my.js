$(document).ready(() => {
  $('.comment-submit').submit((e) => {
    e.preventDefault();
    console.log('form submitted');
    const $this = $(e.currentTarget);
    const rid = $this.data('rid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');
    console.log(`this = ${$this}, rid = ${rid}, csrf = ${csrfmiddlewaretoken}`);

    $.ajax({
      type: 'POST',
      url: `/pages/review/${rid}/comment/`,
      data: {
        rid: rid,
        csrfmiddlewaretoken: csrfmiddlewaretoken,
        content: $(`input#${rid}[name=review-comment]`).val(),
      },
      dataType: 'json',
      success: function(response) {
        console.log(response);
        const username = response.username;
        const content = response.content
        const str = `
        <div>작성자: ${ username } | ${ content }</div>
        `;

        // 만든 댓글을 주입. this는 댓글을 입력하는 input을 의미하므로 this 이후에 댓글이 달리게 함.
        $(str).insertAfter($this);

        // 만들어주고, 새롭게 보여주기까지 했으면 댓글 입력창을 비워줘야 한다.
        $(`input#${rid}[name=review-comment]`).val('');
      },
      error: function(response, status, error) {
        console.log(response, status, error);
      },
      complete: function(response) {
        console.log(response);
      }
    });
  })
})