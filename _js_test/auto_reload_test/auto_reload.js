// ページをreloadする方法
// reloadの基本的な使い方
var count = 0
function doReload() {
 
    // reloadメソッドによりページをリロード
    window.location.reload();
    excuteReloadAfter();
}
 
window.addEventListener('load', function () {
 
    // ページ表示完了した5秒後にリロード
    setTimeout(doReload, 5000);
});

function excuteReloadAfter(){
    el = document.getElementById("text1");
    buf = '';
    buf = el.innerHTML;
    if (buf.indexOf('reloaded ')<0){
        buf = buf + ' reloaded ' + String(count);
        el.innerHTML = buf
    } else{
        el.innerHTML = buf.slice(0,-1) + String(count);
    }
    count = count + 1;
    console.log('buf='+buf + '  count=' + String(count))
}