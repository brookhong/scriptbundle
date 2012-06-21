// ==UserScript==
// @name         sync links
// @namespace    syncLinks
// @include      *
// @author       brook hong
// @description  This userscript is meant to be an example on how to use jQuery in a userscript on Google Chrome.
// ==/UserScript==

function main() {
    var links = new Array();
    var flag = 0;
    $('body').append("<div style='border:2px solid #ccc;border-radius:5px;position:absolute;z-index:1996;top:0;padding:0px 5px 0px 5px;cursor:pointer;display:none;font-size:12px;background:#39e;' id='syncLinks_links'></div>");
    var links_view = $('#syncLinks_links');
    function updateLink() {
        if(flag) {
            lnk = links.join('\n');
            $.getJSON(
                "http://query.yahooapis.com/v1/public/yql?q=update%20yql.storage%20set%20value%3D%22"+
                encodeURIComponent(lnk)+
                "%22%20where%20name%3D%22store%3A%2F%2FHKO7HaS9bdV0BCNGxFc7Mm%22%0A&callback=?",
                function (data) {
                    if ("<success>Updated store://Vmc4iPjC1oITXpnN42IZtU</success>" == data.results[0]) {
                        flag = 0;
                        links_view.css('background','#39e');
                        var evt = document.createEvent("HTMLEvents");
                        evt.initEvent("click", true, true);
                        (links_view.find('a')[0]).dispatchEvent(evt);
                    }
                }
            );
        }
    }
    setInterval(updateLink,5000);

    $('a').click(function () {
        lnk = $(this).attr('href');
        if (links.indexOf(lnk) == -1) {
            links.push(lnk);
            flag = 1;
            links_view.css('background','#f00');
            links_view.html("<p><a href='"+links[0]+"' target='_blank'>"+links[0]+"</a></p><ul><li>"+links.join("</li><li>")+"</li></ul>");
            if(links_view.css('display') == 'none') {
                links_view.fadeTo('fast',0.7);
            }
            return false;
        }
        return true;
    });
}

function addJQuery(callback) {
    var script = document.createElement("script");
    script.setAttribute("src", "http://code.jquery.com/jquery-latest.js");
    script.addEventListener('load', function() {
        var script = document.createElement("script");
        script.textContent = "(" + callback.toString() + ")();";
        document.body.appendChild(script);
    }, false);
    document.body.appendChild(script);
}

addJQuery(main);
