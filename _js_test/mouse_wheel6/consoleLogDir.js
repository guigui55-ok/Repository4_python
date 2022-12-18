

function getDir(place, n) {
    buf = new RegExp("(?:\\\/+[^\\\/]*){0," + ((n || 0) + 1) + "}$")
    return place.pathname.replace(buf, "/");
}


function getDirName(place, n) {
    buf = new RegExp("(?:\\\/+[^\\\/]*){0," + ((n || 0) + 1) + "}$")
    return place.pathname.replace(buf, "/");
}

function consoleLogDirMain(){
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
    console.log('dirName = '+ str);
}

function consoleLogDirMain2(){
    // 'use strict';
    var local = window.location;
    // console.log('local = ' + local);
    var url = local.origin;
    // console.log('url = ' + url);
    url = getDir(local); // 現在のディレクトリ
    // console.log('url = ' + url);
    url = getDir(local,1); // 1つ上のディレクトリ
    // console.log('url = ' + url);
    var str = window.location.href.split('/').pop();
    let ary = window.location.href.split('/');
    ary.length = ary.length-1;
    str = ary.pop();
    console.log('str = '+ str);
}

consoleLogDirMain2();