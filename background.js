chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    if(changeInfo.status == "complete") {
        console.log("finished loading");
        //console.log(changeInfo.url);
    }
    chrome.tabs.query({'active': true, 'currentWindow': true}, function (tabs) {
        var turl = tabs[0].url;
        
        chrome.tabs.sendMessage(tabs[0].id, "hello", function(response) {});

        console.log(turl);
    });
});