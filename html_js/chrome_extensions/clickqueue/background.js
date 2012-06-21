var settings = {
    set:function (key, value) {
            localStorage[key] = value;
        },
    get:function (key) {
            return localStorage[key];
        }
};
var linksFromTabId = [];
var tabIdFromLink = [];
var flag = false;

chrome.browserAction.onClicked.addListener(function(tab) {
    if (!(tab.id in linksFromTabId)) {
        linksFromTabId[tab.id] = [];
    }
    if(linksFromTabId[tab.id].length) {
        finishPage(tab.id);
    }
    else {
        chrome.tabs.executeScript(null, {code:'onClicked()'});
    }
});
chrome.tabs.onRemoved.addListener(function(tabId, removeInfo) {
    if (tabId in linksFromTabId) {
        delete linksFromTabId[tabId];
    }
});
function finishPage(tId) {
    url = linksFromTabId[tId].shift();
    chrome.tabs.executeScript(tabIdFromLink[url], {code:'onPageFinished()'});
    delete tabIdFromLink[url];
    titleString = Object.keys(linksFromTabId).length+"#"+Object.keys(tabIdFromLink).length+"#"+linksFromTabId[tId].length;
    chrome.browserAction.setTitle({title:titleString, tabId:tId});
    if(linksFromTabId[tId].length) {
        ul = linksFromTabId[tId][0];
        chrome.tabs.create({url:ul, active:false},function(tab){
            chrome.tabs.executeScript(tab.id, {code:'onPageCreated("'+ul+'",'+settings.get('TimeLimit')+')'});
        });
    }
    else {
        flag = false;
    }
}
chrome.extension.onRequest.addListener(function(req,from) {
    if(req.method == "setIcon") {
        chrome.browserAction.setIcon({path:"icon" + req.icon + ".png", tabId:from.tab.id});
    }
    else if(req.method == "addLink") {
        linksFromTabId[from.tab.id].push(req.link);
        tabIdFromLink[req.link] = from.tab.id;
        titleString = Object.keys(linksFromTabId).length+"#"+Object.keys(tabIdFromLink).length+"#"+linksFromTabId[from.tab.id].length;
        chrome.browserAction.setTitle({title:titleString, tabId:from.tab.id});
        if(!flag) {
            flag = true;
            ul = linksFromTabId[from.tab.id][0];
            chrome.tabs.create({url:ul, active:false},function(tab){
                chrome.tabs.executeScript(tab.id, {code:'onPageCreated("'+ul+'",'+settings.get('TimeLimit')+')'});
            });
        }
    }
    else if(req.method == "finishPage") {
        console.log(req.url+" finishPage!");
        if(req.url in tabIdFromLink) {
            tId = tabIdFromLink[req.url];
            finishPage(tId);
        }
    }
});
