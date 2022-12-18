
var targetClassName = 'procedureb';
var targetClassNameChild = 'inner_frame';

console.log('horizon_scroll')

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
    console.log("onmousewheel");
    try{
        el = getElementForHorizonScroll(gHoverElement, targetClassName)
        if (e.deltaX === 0) {
            console.log("test_wheel2");
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
    try{
        console.log("window.onload");
        let els = document.getElementsByClassName(targetClassName);
        console.log('els.length = '+ els.length);
        for (let i = 1; i < els.length; i++){

            t_el = els[i];
            print(t_el.className)
            print(targetClassNameChild)
            let child_el = t_el.getElementByClassName(targetClassNameChild);
            print(child_el)
            print(child_el.className)
            child_el.onmousewheel = test_wheel2;
            t_el.onmousewheel = test_wheel2;
            t_el.addEventListener('onmousewheel', test_wheel2)
        }
        // els.forEach(element => {
        //     let child_el = element.getElementByClassName(targetClassNameChild);
        //     child_el.onmousewheel = test_wheel2;
        // });
    } catch(e){
        console.log(e.message);
    }
    console.log("window.onload end");
}

window.addEventListener('load', window_onload);