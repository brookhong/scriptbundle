var myid = chrome.i18n.getMessage("@@extension_id");
var links = [];
var view = null;
var loaded = false;
var internal_url = "";
var start_time = 0;

function jackLink() {
    url = jQuery(this)[0].href;
    if (! /http:\/\/bbs8899.net\/wz.aspx.*/i.test(url)) {
        return true;
    }
    if (links.indexOf(url) == -1) {
        jQuery(this).css('color','#39e');
        links.push(url);
        chrome.extension.sendRequest({method:'addLink',link:url});
        jQuery('#'+myid+'_view').append("<li>"+url+"</li>");
    }
    return false;
}
function onClicked() {
    ic = 0;
    if(view == null) {
        jQuery('body').append("<div style='border:2px solid #ccc;border-radius:5px;position:fixed;z-index:1996;top:0;padding:0px 5px 0px 5px;cursor:pointer;display:none;font-size:12px;background:#39e;' id='"+myid+"_view'></div>");
        view = jQuery('#'+myid+'_view');
        view.fadeTo('fast',0.7);
        jQuery('a').click(jackLink);
        ic = 1;
    }
    else {
        view.remove();
        view = null;
        jQuery('a').unbind('click');
        ic = 0;
    }
    chrome.extension.sendRequest({method:'setIcon',icon:ic});
}
jQuery(document).ready(function() {
    if (/http:\/\/bbs8899.net\/sort.aspx.*/i.test(document.URL)) {
        jQuery('body').append("<div style='border:2px solid #ccc;border-radius:5px;position:fixed;z-index:1996;top:0;padding:0px 5px 0px 5px;cursor:pointer;display:none;font-size:12px;background:#39e;' id='"+myid+"_view'></div>");
        view = jQuery('#'+myid+'_view');
        view.fadeTo('fast',0.7);
        jQuery('a').click(jackLink);
        chrome.extension.sendRequest({method:'setIcon',icon:1});
    }
});
function onPageFinished() {
    if(links.length) {
        links.shift();
        fi = jQuery('#'+myid+'_view').find('li').first();
        fi.fadeOut(300);
        fi.remove();
    }
}
function onPageCreated(url, timeLimit) {
    internal_url = url;
    start_time = (new Date()).getTime();
    console.log(url+" onPageCreated: "+timeLimit);

    jQuery(window).load(function() {
        start_time = (new Date()).getTime()-start_time;
        console.log(internal_url+" loaded, used "+start_time+" milliseconds!");
        loaded = true;
        chrome.extension.sendRequest({method:'finishPage',url: internal_url});
    });

    if(timeLimit > 100) {
        setTimeout(function () {
            if(!loaded) {
                console.log(internal_url+" timeout!");
                window.stop();
                loaded = true;
                chrome.extension.sendRequest({method:'finishPage',url: internal_url});
            }
        },timeLimit);
    }
}
