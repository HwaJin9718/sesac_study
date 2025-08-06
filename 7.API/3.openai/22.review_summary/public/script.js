async function submitReview() {
    const rating = document.querySelector('input[name="rating"]:checked');
    const opinion = document.getElementById('opinion').value;

    if (!rating || !opinion.trim()) {
        alert('평점 또는 후기 내용이 입력되지 않았습니다.');
        return;
    }

    const review = {
        rating: parseInt(rating.value),
        opinion
    }

    const response = await fetch('/api/reviews', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(review)
    });
    const data = await response.json()
    console.log(data)

    // 내가 쓴 글 및 AI 요약 요청
    fetchReviews();
    fetchAISummary();
}

async function fetchReviews() {
    // 모든 fetch는 try catch 로 감싸야함
    const response = await fetch('/api/reviews');
    if (!response.ok) {
        throw new Error('요청 오류');
    }
    const data = await response.json();
    reviews = data.reviews
    console.log(reviews);

    if (reviews) {
        displayReviews(reviews)
    }
}

function displayReviews(reviews) {
    // console.log(reviews);
    const reviewsContainer = document.getElementById('reviews-container')
    // 기존에 작성된 후기글들 지우고 새로 그리기
    reviewsContainer.querySelectorAll('.review-box').forEach(box => box.remove())

    reviews.forEach(review => {
        // console.log(review.rating)
        // console.log(review.opinion)
        const new_div = document.createElement('div')
        new_div.setAttribute('class', 'review-box')
        const new_p1 = document.createElement('p')
        new_p1.setAttribute('class', 'review-header')
        new_p1.textContent = 'Rating : ' + review.rating
        
        const new_p2 = document.createElement('p')
        new_p2.textContent = review.opinion
        
        new_div.appendChild(new_p1)
        new_div.appendChild(new_p2)
        reviewsContainer.appendChild(new_div)
    })
}

async function fetchAISummary() {
    const lang = document.getElementById('languageSelect').value;
    const response = await fetch(`/api/ai-summary?lang=${lang}`);

    // 오류 처리 생략 -> 원래 해야함
    const data = await response.json();
    console.log(data);
    displayAISummary(data);
}

function displayAISummary(data) {
    const summaryBox = document.querySelector('.ai-summary');

    // 기존에 작성된 AI 요약 및 평균 지우고 새로 작성
    summaryBox.querySelectorAll('p').forEach(p => p.remove())

    const new_p1 = document.createElement('p')
    const strong1 = document.createElement('strong')
    strong1.textContent = 'AI 요약:'
    new_p1.appendChild(strong1)
    // textContent 로 사용 시 "AI 요약:"" 문장이 사라지고 data.summary만 남음
    // new_p1.textContent = data.summary
    new_p1.appendChild(document.createTextNode(data.summary)); // 대체 createTextNode
    summaryBox.appendChild(new_p1)

    const new_p2 = document.createElement('p')
    const strong2 = document.createElement('strong')
    strong2.textContent = '평균 별점:'
    new_p2.appendChild(strong2)
    // new_p2.textContent = data.averageRating.toFixed(2)
    new_p2.appendChild(document.createTextNode(data.averageRating.toFixed(2)));
    summaryBox.appendChild(new_p2)

    // summaryBox.innerHTML = `
    // <p><strong>AI 요약:</strong> ${data.summary}</p>
    // <p><strong>평균 별점:</strong> ${data.averageRating.toFixed(2)}</p>
    // ` // toFixed(2) -> 소수점 2자리까지 보여주기
}

document.addEventListener('DOMContentLoaded', async () => {
    await fetchReviews();
    await fetchAISummary();
})

// 위랑 동일 기능, 강사님꺼
// window.onload = async () => {
//     await getReviews();
//     await fetchAISummary();
// }