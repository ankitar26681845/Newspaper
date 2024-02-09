$(document).ready(function () {
    // Load articles dynamically
    $.getJSON('/get_articles', function (data) {
        var articlesContainer = $('#articles-container');
        $.each(data.articles, function (index, article) {
            articlesContainer.append(
                '<article>' +
                '<h2><a href="/article/' + article.id + '">' + article.title + '</a></h2>' +
                '<p>' + article.summary + '</p>' +
                '</article>'
            );
        });
    });

    // Form validation example
    $('#submit-form').submit(function (event) {
        var title = $('#title').val();
        var content = $('#content').val();

        if (!title || !content) {
            alert('Please fill in all fields');
            event.preventDefault();
        }
    });
});