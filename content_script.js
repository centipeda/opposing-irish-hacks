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
            class Article {
                constructor(u, t) {
                    this.url = u;
                    this.title = t;
                }
            }
            article = {
                url: "https://www.npr.org/2019/11/09/777914177/republicans-ask-for-whistleblower-hunter-biden-to-testify-in-impeachment-inquiry",
                title: "Republicans Ask For Whistleblower, Hunter Biden To Testify In Impeachment Inquiry"
            }

            console.log(result);
        }
    );
  });

$(function() {
    $("#closebutton").click(function() {
    // console.log("clicked");
    console.log($("#mainbox").fadeOut());
    // $("#mainbox").css("background-color", "blue");
    });
});