// console.log("testing"); 
$.get(chrome.extension.getURL("news_box.html"), function(data) {
    // console.log("getting data");
    $("body").prepend(data);
    // console.log("sending GET...");
});


function loadArticles (articles) {
    
}

chrome.extension.onMessage.addListener(function(msg, sender, sendResponse) {
    // console.log(msg);
    // console.log("sending GET...");
    var encodedURL = encodeURIComponent(msg);
    // console.log(encodedURL);
    fetch("https://centipeda.cc/test/get/" + encodedURL,
        {
            // mode: "no-cors",
            method: "GET"
        }).then( (res) => res.json()).then( (result) => {
            // result will be a list of objects that have
            // properties like: url, title...

            console.log(result);
        }
    );
  });

$(function() {
    $("#closebutton").click(function() {
    // console.log("clicked");
    //console.log($("#mainbox").fadeOut());
    // $("#mainbox").css("background-color", "blue");
    class Article {
        constructor(u, t, b) {
            this.url = u;
            this.title = t;
            this.bias = b;
        }
    }
    
    article1 = new Article ("https://www.foxnews.com/politics/trump-brushes-off-witch-hunt-impeachment-probe", "Trump wants Pelosi, Biden to be called as impeachment inquiry witnesses, says he'll release second phone call transcript", "right");
    article2 = new Article ("https://www.nbcnews.com/politics/trump-impeachment-inquiry/only-3-senate-republicans-aren-t-defending-trump-impeachment-inquiry-n1078906", "Only 3 Senate Republicans aren't defending Trump from the impeachment inquiry. Here's why.", "left");
    article3 = new Article ("https://www.cbsnews.com/news/trump-impeachment-inquiry-recap-house-releases-testimony-transcripts-prepares-public-hearings-2019-11-09/", "What happened in the impeachment inquiry this week", "neutral");

    //article1.title="Trump wants Pelosi";
    var articles = [article1, article2, article3];


    for (x in articles) {
        var t = "<h4>" + x.title + "</h4>";
        var u = "<a href=\"" + x.url + "\">" + x.url + "</a>";
        var b = "<p>Bias of article: " + x.bias + "</p>";
        $("#morenews").append(t, u, b);
    };
            
    });
});