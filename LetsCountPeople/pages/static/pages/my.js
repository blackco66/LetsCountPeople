$(document).ready(() => {
  $('.comment-submit').submit((e) => {
    e.preventDefault();
    console.log('form submitted');
    const $this = $(e.currentTarget);
    const rid = $this.data('rid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

    $.ajax({
      type: 'POST',
      url: `/pages/review/${rid}/comment/`,
      data: {
        rid: rid,
        csrfmiddlewaretoken: csrfmiddlewaretoken,
        content: $(`input#${rid}[name=comment]`).val()
      },
      dataType: 'json',
      success: function(response) {
        console.log(response);
        const username = response.username;
        const content = response.content;
        const cid = response.id;
        const str = `
        <div class="review-comment"
          <div class="review-comment"><strong>${ username }</strong> | ${ content }</div>
          {% if request.user == comment.author %}
            <a href="/pages/review/${ rid }/comment/${ cid }/delete/">삭제</a>
          {% endif %}
        </div>
        `;

        // 만든 댓글을 주입. this는 댓글을 입력하는 input을 의미하므로 this 이후에 댓글이 달리게 함.
        $(str).insertBefore($this);

        // 만들어주고, 새롭게 보여주기까지 했으면 댓글 입력창을 비워줘야 한다.
        $(`input#${rid}[name=comment]`).val('');
        content.trigger( "create" ); // 이런 코드를 넣으면 되는 것 같은데,,, 어떻게 넣어야 하는건지 잘 모르겠으!!
      },
      error: function(response, status, error) {
        console.log(response, status, error);
        console.log(response.content);
      },
      complete: function(response) {
        console.log(response);
      }
    });
  })
})