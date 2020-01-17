function getNewQuote() {
    fade()
    // TODO get new quote
    var twitterLink = "https://twitter.com/intent/tweet?text=\"" +
    linkQuote + "\"%20%20%20&hashtags=" + linkMovie + ",freeCodeCamp" +
    ",FrontEndWebDev"
    $("#tweet-link").attr("href", twitterLink);
}

function fade() {
    $(".quote").fadeOut(1000, function () {
        $(".quote").html("\"" + quote + "\"");
        $(this).fadeIn(1000);
    });

    $(".movie").fadeOut(1000, function () {
        $(".movie").html("- " + movie);
        $(this).fadeIn(1000);
    });

    $(".btn-basic").fadeOut(1000, function () {
        $(this).fadeIn(1000);
    })
};
