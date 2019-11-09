console.log("testing"); 
$.get(chrome.extension.getURL("news_box.html"), function(data) {
    console.log("getting data");
    $("body").prepend(data);
});
