chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    if(changeInfo.status == "complete") {
        console.log("finished loading");
        //console.log(changeInfo.url);
    }
    chrome.tabs.query({'active': true, 'currentWindow': true}, function (tabs) {
        var url = tabs[0].url;
        console.log(url);
    });
});