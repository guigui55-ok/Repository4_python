
console.log('script in file')


function test(){
    var id = 'procedure1';
    var base_el = document.getElementById(id);
    console.log(base_el);
    var child_nodes_count = base_el.childElementCount;
    console.log('cont = ' + child_nodes_count);
    var length = 0;
    var el = undefined;
    for(let i=0; i<child_nodes_count; i++) {
        el = base_el.children[i];
        // console.log(el.textContent);
        console.log('tagName  =' + el.tagName);
        if (el.tagName=='P'){
            console.log(el.clientWidth);
            length += el.clientWidth;
            console.log(length);
        }
    }
    console.log('el.length = ' + length);
    length = length * 1.1;

    var el = document.querySelector('.procedure_details div');
    console.log('class name = ' + el.className);
    console.log('id = ' + el.id);
    window.document.getElementById(el.id).style.width = length + 'px';
    var val = 'procedure_details1';
    // window.document.getElementById(val).style.width = length + 'px';
}
window.onload = function() {
    console.log("ページ読み込み完了");
    test();
}