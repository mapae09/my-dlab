var content= "Andy's Home" // 사용할 문구
var text = document.querySelector('#typing-text')
var index = 0; // 문자열 인덱스

function typing() {
    text.textContent += content[index++];
    if(index > content.length){
        text.textContent = "";
        index = 0;
    }
}
setInterval(typing, 200); // 타이핑 시간 설정(글자 하나당 시간)