function change_action(id) {
    var form = $("#id_form_comment_add");
    var action = '/add_comment/';
    form.data("x_comment_id", id);
    form.attr("action", action+id);
}

function send_comments() {
    var form = $("#id_form_comment_add");
    var url = form.attr("action");
    var formData = $(form).serializeArray();
    $.post(url, formData)
        .done(function (data) {
            form.trigger('reset');
            $("#id_comment_"+form.data("x_comment_id")).replaceWith(data['result_html']);
        })
        .fail(function (data) {
            alert(data)
        });
}