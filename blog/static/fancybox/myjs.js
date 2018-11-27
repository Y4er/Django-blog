$(function () {
    // js 解析markdown
    editormd.markdownToHTML("post-content", {
        //htmlDecode      : "style,script,iframe",  // you can filter tags decode
        emoji: true,
        taskList: true,
        tex: true,  // 默认不解析
        flowChart: true,  // 默认不解析
        sequenceDiagram: true,  // 默认不解析
    });

    $(".reference-link").each(function (i, obj) {
        console.log(obj);
    })
});
// 未解决Cannot read property 'getAttribute' of undefined
window.onload = function () {
    var postContent = document.getElementById("post-content");
    var imgs = postContent.getElementsByTagName("img");
    console.log(imgs.length);
    for (var i = 0; i <= imgs.length; i++) {
        var imgurl = imgs[i].getAttribute("src");
        imgs[i].outerHTML = "<a class=\"fancybox\" rel=\"group\" href=" + imgurl + " >" + imgs[i].outerHTML + "</a>";
    }
};

$(document).ready(function () {
    $(".fancybox").fancybox();
});
