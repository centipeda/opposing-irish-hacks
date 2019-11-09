console.log("testing"); 
$.get(chrome.extension.getURL("news_box.html"), function(data) {
    console.log("getting data");
    // $("#body").prepend(data);
    newsbox = Boundary.createBox("mainbox");
    Boundary.appendToBox("#mainbox", data);
    Boundary.loadBoxCSS("#mainbox", chrome.extension.getURL("ext/material.min.css"));
});
