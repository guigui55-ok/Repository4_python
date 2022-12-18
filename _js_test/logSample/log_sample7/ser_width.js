

// window.onload = function(){
//     // SCRIPTタグの生成
//     var el = document.createElement("script"); 
//     // SCRIPTタグのSRC属性に読み込みたいファイルを指定
//     el.src = "common.js"; 
//     // BODY要素の最後に追加
//     document.head.appendChild(el);
// }

// document.write('<script src="common.js"></script>');
_DEBUG = true
function console_log(value){
    if (_DEBUG){
        console.log(value);
    }
}

const FRAME_CLASS_NAME = 'test_box'
const CHANGE_WIDTH_CLASS_NAME = 'wheel_test_inner'


console_log('set_width')

function test2(){
    var base_id = 'box'
    seach_element_by_id_with_number(base_id, 11)
}

function seach_element_by_id_with_number(base_id, max=10){
    var id='';
    var child_class_name = FRAME_CLASS_NAME
    // child_class_name = 'wheel_test_inner'
    var change_width_class_name = CHANGE_WIDTH_CLASS_NAME
    for(let i=1; i<max; i++) {
        id = base_id + String(i);
        var base_el = document.getElementById(id);
        if (base_el==null){break;}
        length = count_length_child_element(base_el, child_class_name);
        // length = Number(length /2)
        console.log('id = %s,length = %d',id,length);
        // length = Number(length * 1.1);
        length = Number(length * 1.01);
        // length = Number(length * 0.5);
        set_width_child_element_by_class_name(base_el, change_width_class_name, length)
    }
}


function set_width_child_element_by_class_name(parent_element, class_name, width){
    var el = parent_element.querySelector('.' + class_name);
    // window.document.getElementById(el.id).style.width = length + 'px';
    el.style.width = length + 'px';
    console.log('class name = %s , length = %d', el.className, length);
}

function count_length_child_element(element, child_class_name){
    var length = 0;
    var child_nodes_count = element.childElementCount;
    var for_el = undefined;
    // for(let i=0; i<child_nodes_count; i++) {
    //     for_el = element.children[i];
    //     if (for_el.className==child_class_name){
    //         console.log(for_el.clientWidth);
    //         length += for_el.clientWidth;
    //         console.log(length);
    //     }
    // }
    var elements = document.querySelectorAll('.'+child_class_name);
    el_count = elements.length
    for(let i=0; i<el_count; i++) {
        for_el = elements[i];
        if (for_el.className==child_class_name){
            length += for_el.clientWidth;
            // console.log(for_el.clientWidth);
            // console.log(length);
        }
    }
    return length;
}

function test(){
    var id = 'box';
    var base_el = document.getElementById(id);
    if (base_el==null){ return;}
    console.log(base_el);
    var child_nodes_count = base_el.childElementCount;
    console.log('cont = ' + child_nodes_count);
    var length = 0;
    var el = undefined;
    for(let i=0; i<child_nodes_count; i++) {
        el = base_el.children[i];
        if (el.className=='test_box'){
            console.log(el.clientWidth);
            length += el.clientWidth;
            // console.log(length);
        }
    }
    console.log('el.length = ' + length);
    length = length * 1.1;

    var els = document.querySelector('.procedureb');
    console.log('class name = ' + el.className);
    console.log('id = ' + el.id);
    window.document.getElementById(el.id).style.width = length + 'px';
    var val = 'procedure_details1';
}

window_onload = function() {
    console.log("ページ読み込み完了");
    test2();
    // test();
}
window.addEventListener('load', window_onload);