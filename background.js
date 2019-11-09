chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    if(changeInfo.status == "complete") {
        console.log("finished loading");
    }
    chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
        var url = tabs[0].url;
        console.log(url);
    });
});