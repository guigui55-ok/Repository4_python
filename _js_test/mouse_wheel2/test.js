

function getDir(place, n) {
    buf = new RegExp("(?:\\\/+[^\\\/]*){0," + ((n || 0) + 1) + "}$")
    return place.pathname.replace(buf, "/");
}

// 'use strict';
var local = window.location;
console.log('local = ' + local);
var url = local.origin;
console.log('url = ' + url);
url = getDir(local); // 現在のディレクトリ
console.log('url = ' + url);
url = getDir(local,1); // 1つ上のディレクトリ
console.log('url = ' + url);
var str = window.location.href.split('/').pop();
let ary = window.location.href.split('/');
ary.length = ary.length-1;
str = ary.pop();
console.log('str = '+ str);

function getDirName(place, n) {
    buf = new RegExp("(?:\\\/+[^\\\/]*){0," + ((n || 0) + 1) + "}$")
    return place.pathname.replace(buf, "/");
}

window.onmousewheel = function(){
	// if(event.wheelDelta > 0){
	// 	//mainCamera.zoomTo(4, 100);
    //     // y=500の位置までスクロール
    //     console.log('wheelDelta = ' + wheelDelta);
    //     document.documentElement.scrollTop = 500;
	// }else{
	// 	//mainCamera.zoomTo(1, 100);
	// }

}

// document.addEventListener("mouseover", mouseover_event);
function mouseover_event(e){
    // console.log('mouseover_event')
    console.log(e.target.tagName); //event.targetの部分がマウスオーバーされている要素になっています
}

function test_wheel(e) {
    // var buf = e.deltaY;
    // document.addEventListener("mouseover", function(event) {
    //     console.log(event.target.tagName); //event.targetの部分がマウスオーバーされている要素になっています
    // })
    // document.onmouseover = mouseover_event
    // document.onmouseover -= mouseover_event
    // document.removeEventListener('mouseover', mouseover_event);
    // document.onmouseover = document.onmouseover - mouseover_event
    // scrollTo(0, 500);
    // try{
    //     if (e.deltaX === 0) {
    //         var y = e.deltaY;
    //         e.stopPropagation();
    //         e.preventDefault();
    //         // noinspection JSSuspiciousNameCombination
    //         window.scrollBy(y, 0);
    //         console.log('test_wheel  data = ' + y);
    //     }
    // } catch(ex){
    //     console.log(ex.message);
    // }
}


// var class_name_selector = '.common-x-scroll';
// var class_name_selector = '.wheel_test';
// var cxs = document.querySelectorAll(class_name_selector);
// cxs = Array.prototype.slice.call(cxs, 0);
// cxs.forEach(function(el){
//   el.addEventListener("mousewheel",function(e){
//     if (e.deltaX === 0) {

//         var reg = 1.5;//スクロール量を変更する場合はここを調整
 
//         el.scrollLeft = el.scrollLeft + e.deltaY * reg;
        
//         e.preventDefault();
//         console.log('wheel ' + el.scrollLeft);
//     }
//   });
// });
// var class_name_selector = '.wheel_test';
var gHoverElement = undefined;
var gEl = undefined;
var cl = 'wheel_test';
document.addEventListener("mouseover", function(e) {
    // console.log(event.target); 
    //event.targetの部分がマウスオーバーされている要素になっています
    // gHoverElement = Event.element(e); //xx
    gHoverElement = e.target;
    // console.log(typeof gHoverElement);
    // let ary = ('');
    // for(var item in gHoverElement){
    //     ary.push(item);
    // }
    // console.log(ary);
    // // console.log(gHoverElement.tagName);
    // gEl = getElementForHorizonScroll(gHoverElement, cl);
})

function getElementForHorizonScroll(el, class_name){
    try{
        console.log('getElementForHorizonScroll = ' + el.className);
        if (el.className === class_name){
            return el;
        }
        var parent = el.parentNode;
        if (parent.className === class_name){
            console.log(parent.className);
            return parent;
        } else{
            if (el.className===''){ return NaN;}
            /// 
            console.log(el.className);
            var ret =getElementForHorizonScroll(parent , class_name);
            return ret;
        }
    } catch(ex){
        console.log(ex.message)
    }
}


async function test_wheel2(e){
    try{
        el = gHoverElement;
        console.log('test_wheel2 ' + el.tagName);
        var parent = el.parentNode;
        el = getElementForHorizonScroll(gHoverElement, 'wheel_test')
        console.log('parent = ' + parent);
        if (e.deltaX === 0) {
            var reg = 1.5;//スクロール量を変更する場合はここを調整
     
            el.scrollLeft = el.scrollLeft + e.deltaY * reg;
            
            e.preventDefault();
            console.log('wheel2 ' + el.scrollLeft);
        }
    } catch (ex){
        console.log(ex);
    }
}


window.onload = function() {
    console.log("window.onload");
    let buf = document.getElementsByClassName('wheel_test');
    // console.log('* buf = ')
    // console.log(buf);
    // var flag = Array.isArray(els);
    // console.log(flag);
    // var els = buf.children;
    // console.log('* buf.children = ')
    // console.log(typeof els);
    // console.log(els.length)
    // var flag = Array.isArray(els);
    // console.log(flag);
    els = Array.from(buf) ;
    els.forEach(element => {
        element.onmousewheel = test_wheel2;
    });
}