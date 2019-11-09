chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    if(changeInfo.status == "complete") {
      console.log("finished loading");
      var url;
      var tab_id = tabId.tabId;
      chrome.tabs.get(tab_id, function(tab){
        url = tab.url;
        console.log(url);
      });
        /*chrome.tabs.getCurrent(function(tab){
          console.log(tab.url);
        }
        );*/
        //console.log(changeInfo.url);
        // chrome.tabs.sendMessage(tabs[0].id, changeInfo.url, function(response) {});
    }
    console.info("This is the url of the tab = " + changeInfo.url);
});


/*chrome.tabs.onActivated.addListener(function (tabId) {
  var url;
  var tab_id = tabId.tabId;
  chrome.tabs.get(tab_id, function(tab){
      url = tab.url;
      console.log(url);
  });
});*/

/* /chrome.tabs.query({'active': true, 'currentWindow': true}, function (tabs) {
  var turl = tabs[0].url;
  console.log(activeTabId);

  chrome.tabs.sendMessage(tabs[0].id, "hello", function(response) {});
  // chrome.tabs.sendMessage(tabs[0].id, "url should be: " + turl, function(response) {});
  // chrome.tabs.sendMessage(tabs[0].id, "url should precede this", function(response) {});

  console.log(turl);
});

var activeTabId;

chrome.tabs.onActivated.addListener(function(activeInfo) {
  activeTabId = activeInfo.tabId;
});

function getActiveTab(callback) {
  chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
    var tab = tabs[0];

    if (tab) {
      callback(tab);
    } else {
      chrome.tabs.get(activeTabId, function (tab) {
        if (tab) {
          callback(tab);
        } else {
          console.log('No active tab identified.');
        }
      });

    }
  });
}*/