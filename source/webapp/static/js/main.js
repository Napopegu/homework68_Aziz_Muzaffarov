async function makeRequest(url, method = 'GET') {
    let response = await fetch(url, {method});

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.status);
        error.response = response;
        throw error;
    }

}

async function onClickLike(e) {
    e.preventDefault()
    let button = e.target;
    let articleId = button.dataset['articleId'];
    let data = await makeRequest(`/article/${articleId}/like/`, 'GET');

    if (data.liked) {
        button.innerText = 'Анлайк';
    } else {
        button.innerText = 'Лайк';
    }
    document.getElementById(`likes-count-${articleId}`).innerText = data.likes_count;
}

function onLoad() {
    let likeButtons= document.querySelectorAll('.like-button');
    likeButtons.forEach(button => {
        button.addEventListener('click', onClickLike);
    });
}

window.addEventListener('load', onLoad);