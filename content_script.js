console.log("testing"); 
$.get(chrome.extension.getURL("news_box.html"), function(data) {
    console.log("getting data");
    $("body").prepend(data);
    console.log("sending GET...");

    /*
    fetch("https://centipeda.cc/test/get",
        {
            // mode: "no-cors",
            method: "GET"
        }).then( (res) => res.json()).then( (result) => {
            console.log(result);
        }
    );
        */
});

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
            console.log(result);
        }
    );
  });