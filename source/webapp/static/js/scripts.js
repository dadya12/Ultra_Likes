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

async function onClick(event) {
    event.preventDefault();
    let link = event.target.closest('.like-article, .like-comment');
    let url = link.getAttribute('data-url');
    try {
        let response = await makeRequest(url);
        let span = link.parentElement.querySelector(".like-count");
        span.innerText = `Лайков: ${response.total_likes}`;
        link.querySelector('i').classList.toggle('bi-heart-fill', response.liked);
        link.querySelector('i').classList.toggle('bi-heart', !response.liked);
    } catch (error) {
        console.error("Failed to update like:", error);
    }
}

function onLoad() {
    let links = document.querySelectorAll('.like-article, .like-comment');
    links.forEach(link => {
        link.addEventListener("click", onClick);
    });
}

window.addEventListener("load", onLoad);