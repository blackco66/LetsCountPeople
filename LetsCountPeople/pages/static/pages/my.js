$(document).ready(() => {

  // 새로고침 없이 댓글 생성하는 함수

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
        <div class="review-comment">
          <div><strong>${ username }</strong> | ${ content }</div>
          <form class="comment-delete" data-rid="${ rid }" data-cid="${ cid }" data-csrfmiddlewaretoken="${ csrfmiddlewaretoken }">
            <button type="submit">삭제</button>
          </form>
        </div>
        `;

        // 만든 댓글을 주입. this는 댓글을 입력하는 input을 의미하므로 this 이후에 댓글이 달리게 함.
        
        if ( $('.review-comment').length ) {
          console.log('1');
          $(str).insertAfter($('.review-comment:last'));
        }
        else {
          console.log('2');
          $('.comment-wrapper').prepend(str);
        }
        

        // 만들어주고, 새롭게 보여주기까지 했으면 댓글 입력창을 비워줘야 한다.
        $(`input#${rid}[name=comment]`).val('');
      },
      error: function(response, status, error) {
        console.log('error');
        console.log(response.content);
      },
      complete: function(response) {
        console.log(response);
      }
    });
  });

  // 새로고침 없이 댓글 삭제하는 함수
  // 왜 문제가 없는거지????
  $(document).on('submit', '.comment-delete', function(e) {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const rid = $this.data('rid');
    const cid = $this.data('cid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

    $.ajax({
      type: 'POST',
      url: `/pages/review/${rid}/comment/${cid}/delete/`,
      data: {
        csrfmiddlewaretoken: csrfmiddlewaretoken,
      },
      dataType: 'json',
      success: function(response) {
        console.log('success');
        $this.parent().remove();
      },
      error: function(response, status, error) {
        console.log('error');
        console.log(response, status, error);
      },
      complete: function(response) {
        console.log(response);
      }
    });
  });

  // 리뷰 추천할 때 redirect 없이 추천 div 영역만 새로고침하는 함수
  $('.feed-rec').click( (e) => {
    e.preventDefault();

    const $this = $(e.currentTarget);
    const id = $this.data('id');
    const rid = $this.data('rid');

    $.ajax({
      type: 'GET',
      url: `/pages/review/${rid}/rec/`,
      data: {
        id: id,
        rid: rid,
      },
      dataType: 'json',
      success: function(response) {
        const str = `추천: ${response.count}`
        $this.html(str)
      },
      error: function(response, status, error) {
        console.log('error');
        console.log(response, status, error);
      },
      complete: function(response) {
      }
    })
  })
})

