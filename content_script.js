console.log("testing"); 
$.get(chrome.extension.getURL("news_box.html"), function(data) {
    console.log("getting data");
    $("body").prepend(data);
});

chrome.extension.onMessage.addListener(function(msg, sender, sendResponse) {
    console.log(msg);
  });
