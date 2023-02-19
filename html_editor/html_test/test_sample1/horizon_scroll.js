
// 横スクロールをホイールでする対象クラス名
var targetClassName = 'wheel_test';
var targetClassName2 = 'proceure_box_b';
var targetClassName3 = 'inner_frame';
let targetClassNames = [
    'wheel_test','proceure_box_b','inner_frame'
]
// event追加用のグローバル変数
let gTargetClassNames = [];
var gHoverElement = undefined;
function saveMouseOverElement(e){
    gHoverElement = e.target;
}

function console_log(value){
    console.log(value);
}

document.onmouseover = saveMouseOverElement;

function getElementForHorizonScroll(el, class_names){
    try{
        if (el.tagName === 'body'){
            console_log('el.tagName === body ===nothing')
            return;}
        if (isMatchClassNames(el, class_names)){
            return el;
        }
        // 親要素を再帰的に検索して合致したら要素を返す
        var parent = el.parentNode;
        var ret = getElementForHorizonScroll(parent, class_names);
        return ret;
    } catch(ex){
        console_log(ex.message)
    }
}

function getIndexMatchClassNames(el, class_names){
    var idx = class_names.findIndex(
        element=>el.className === element
    );
    if (idx>=0){
    }
    return idx;
}

function isMatchClassNames(el ,class_names){
    var idx = getIndexMatchClassNames(el, class_names);
    if (idx<0){
        return false;
    }
    return true
}

// ホイールイベントが発生したときの処理
function event_horizon_scroll(e){
    try{
        el = getElementForHorizonScroll(gHoverElement, gTargetClassNames)
        
        if (el===undefined){return;}
        if (e.deltaX === 0) {
            //スクロール量を変更する場合はここを調整
            var reg = 1.5;
            ret = 1;     
            el.scrollLeft = el.scrollLeft + e.deltaY * reg;            
            e.preventDefault();
        }
    } catch (ex){
        console_log(ex);
    }
}

// ホイールイベントを追加する
function add_event_horizon_scroll (class_name){
    gTargetClassNames[gTargetClassNames.length] = class_name
    try{
        let buf = document.getElementsByClassName(class_name);
        els = Array.from(buf);
        els.forEach(element => {
            element.onmousewheel = event_horizon_scroll;
        });
    } catch(e){
        console_log(e.message);
    }
}

// function add_event_to_child_horizon_scroll (class_name, target){
//     try{
//         add_event_horizon_scroll(class_name);
//         add_event_horizon_scroll(target);
//     } catch(e){
//         console_log(e.message);
//     }
// }

window_onload = function() {
    for (let i = 0; i < targetClassName.length; i++){
        add_event_horizon_scroll(targetClassNames[i]);
    }
}

window.addEventListener('DOMContentLoaded', window_onload);