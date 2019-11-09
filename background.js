chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    if(changeInfo.status == "complete") {
      console.log("finished loading");
      console.log(tab.url);
      chrome.extension.sendMessage(tab.url, function(){});
    }
    
});