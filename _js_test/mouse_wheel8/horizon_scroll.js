
var targetClassName = 'wheel_test';
let gTargetClassNames = [];

var gHoverElement = undefined;
function saveMouseOverElement(e){
    gHoverElement = e.target;
}
document.onmouseover = saveMouseOverElement;

function getElementForHorizonScroll(el, class_names){
    try{
        // if (el.className === ''){ return;}
        // var idx = getIndexMatchClassNames(el, class_names)
        // var class_name = class_names[idx];
        if (el.tagName === 'body'){
            console.log('nothing')
            return;}
        if (isMatchClassNames(el, class_names)){
            return el;
        }
        // 親要素を再帰的に検索して合致したら要素を返す
        var parent = el.parentNode;
        var ret = getElementForHorizonScroll(parent, class_names);
        return ret;
        // if (isMatchClassNames(parent,class_names)){
        //     return parent;
        // } else{
        //     if (parent.className === ''){ return;}
        //     var ret = getElementForHorizonScroll(parent , class_name);
        //     return ret;
        // }
    } catch(ex){
        console.log(ex.message)
    }
}

function getIndexMatchClassNames(el, class_names){
    var idx = class_names.findIndex(
        element=>el.className === element
    );
    if (idx>=0){
        console.log('idx = ' + idx)
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

function event_horizon_scroll(e){
    try{
        el = getElementForHorizonScroll(gHoverElement, gTargetClassNames)
        
        console.log('hover = '+ gHoverElement.className);
        if (el===undefined){return;}
        console.log(el);
        if (e.deltaX === 0) {
            // console.log(`x, y = ${e.deltaX} , ${e.deltaY}`);
            //スクロール量を変更する場合はここを調整
            var reg = 1.5;
            ret = 1;     
            console.log('el.scrollLeft = ' + el.scrollLeft);
            el.scrollLeft = el.scrollLeft + e.deltaY * reg;            
            e.preventDefault();
            console.log('wheel2 = ' + el.scrollLeft);
        }
    } catch (ex){
        console.log(ex);
    }
}

window_onload = function() {
    // console.log("window.onload");
    add_event_horizon_scroll(targetClassName);
    add_event_horizon_scroll('proceure_box_b');
    add_event_horizon_scroll('inner_frame');
    // add_event_to_child_horizon_scroll('proceure_box_b','inner_frame');
}

function add_event_horizon_scroll (class_name){
    console.log('parent class_name = ' +  class_name);
    gTargetClassNames[gTargetClassNames.length] = class_name
    try{
        let buf = document.getElementsByClassName(class_name);
        els = Array.from(buf);
        els.forEach(element => {
            console.log('els = ' +  element.className);
            element.onmousewheel = event_horizon_scroll;
        });
    } catch(e){
        console.log(e.message);
    }
}

function add_event_to_child_horizon_scroll (class_name, target){
    // console.log('class_name = ' +  class_name);
    try{
        add_event_horizon_scroll(class_name);
        add_event_horizon_scroll(target);
        // let buf = document.getElementsByClassName(class_name);
        // els = Array.from(buf);
        // els.forEach(element => {
        //     add_event_horizon_scroll(target)
        //     // let buf2 = document.getElementByClassName(target);
        //     // console.log('buf2 = ' +  buf2);
        //     // buf2.onmousewheel = event_horizon_scroll;
        //     element.onmousewheel = event_horizon_scroll;
        // });
    } catch(e){
        console.log(e.message);
    }
}

// window.addEventListener('load', window_onload);
window.addEventListener('DOMContentLoaded', window_onload);