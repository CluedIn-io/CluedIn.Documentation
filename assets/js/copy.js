$(document).ready(function() {
  $('.highlighter-rouge').each((i, e) => {
    const $button = $('<div style="cursor:pointer;float:right;">Copy</div>');
    $button.click((e) => {
      const text = $(e.target).next().text();
      if (!navigator.clipboard) {
        console.log(text);
      } else {
        navigator.clipboard.writeText(text);
      }
      $button.text('Copied');
      setTimeout(() => {
        $button.text('Copy');
      }, 5000);
    });
  
    $(e).prepend($button);
  });
});

