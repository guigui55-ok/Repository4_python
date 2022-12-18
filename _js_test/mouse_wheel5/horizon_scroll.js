
var targetClassName = 'wheel_test';

var gHoverElement = undefined;
function saveMouseOverElement(e){
    gHoverElement = e.target;
}
document.onmouseover = saveMouseOverElement;

function getElementForHorizonScroll(el, class_name){
    try{
        if (el.className === class_name){
            return el;
        }
        var parent = el.parentNode;
        if (parent.className === class_name){
            return parent;
        } else{
            if (el.className === ''){ return NaN;}
            var ret = getElementForHorizonScroll(parent , class_name);
            return ret;
        }
    } catch(ex){
        console.log(ex.message)
    }
}

function test_wheel2(e){
    try{
        el = getElementForHorizonScroll(gHoverElement, targetClassName)
        if (e.deltaX === 0) {
            //スクロール量を変更する場合はここを調整
            var reg = 1.5;
            ret = 1;     
            el.scrollLeft = el.scrollLeft + e.deltaY * reg;            
            e.preventDefault();
            // console.log('wheel2 ' + el.scrollLeft);
        }
    } catch (ex){
        console.log(ex);
    }
}

window_onload = function() {
    // console.log("window.onload");
    let buf = document.getElementsByClassName(targetClassName);
    els = Array.from(buf) ;
    els.forEach(element => {
        element.onmousewheel = test_wheel2;
    });
}

// window.addEventListener('load', window_onload);
window.addEventListener('DOMContentLoaded', window_onload);