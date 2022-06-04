var num = 0;

// 入室時の処理
function in_room(){
    num++;
    document.getElementById('text').innerHTML = num;

    var time = new Date();
    document.getElementById('time').innerHTML = time;

}

// 退室時の処理
function out_room(){
    if (num > 0){
        num--;
    }
    else{
        alert("人数は0以下になりません")
    }
    document.getElementById('text').innerHTML = num;
}















