async function makeRequest(url, method="GET"){
    let response = await fetch(url, {"method": method});
    if(response.ok){
        return await response.json();
    }
    else{
        let error = new Error(response.text);
        console.log(error);
        throw error;
    }
}

async function onClick(event){
    event.preventDefault();
    let a = event.target;
    let url = a.href;
    let response = await makeRequest(url);
    console.log(a.parentElement)
    let span = a.parentElement.getElementsByTagName("span")[0]
    span.innerText = response.test
    console.log(response)
}

function onLoad(){
    let links= document.querySelectorAll('[data-js="js"]');
    for (let link of links){
        link.addEventListener("click", onClick);
    }
}

window.addEventListener("load", onLoad);