async function getPathToFile(){
    var path = document.getElementById("path").value;
    if(path!=''){
        eel.getPath(path);
        showFiles();
    }else{
        eel.getPath('NoPath');
    }
}

eel.expose(getColors);
function getColors(){
    var colors = document.getElementById("colors").value;
    if(colors!=''){
        return colors;
    }else{
        return 'No';
    }
}

eel.expose(showLog)
function showLog(x) {
    var targetDiv = document.getElementById('filelist');
    if (x !== undefined){
        targetDiv.insertAdjacentHTML('afterbegin', `<div class="message">${x}</div>`);
    }
}

eel.expose(showMD)
function showMD(x) {
    document.getElementById('markdown').innerHTML = marked.parse(x);
}
