

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

function test_wheel() {
    console.log('test_wheel');
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
        element.onmousewheel = test_wheel;
    });
}