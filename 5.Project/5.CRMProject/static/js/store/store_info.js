function get_url_by_id() {
    const url_path = window.location.pathname.split('/') // /를 기준으로 나눠서 url 파라미터 추출
    return url_path[url_path.length - 1] // 추출된 리스트의 마지막 값 리턴
}

function get_store_by_id() {

    const id = get_url_by_id();

    fetch(`/api/store/info/${id}`)
        .then(response => response.json())
        .then(store => {

            const storeResultDiv = document.getElementById('store_result');
            storeResultDiv.innerHTML = ""; // 기존 데이터 제거

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'store_table');
            const new_th_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "NAME"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "Type"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "ADDRESS"

            new_th_tr.appendChild(new_th1)
            new_th_tr.appendChild(new_th2)
            new_th_tr.appendChild(new_th3)
            new_table.appendChild(new_th_tr)
            storeResultDiv.appendChild(new_table)

            const store_table = document.getElementById('store_table');
            const new_tb_tr = document.createElement('tr')

            const new_td1 = document.createElement('td')
            new_td1.textContent = store.store.Name

            const new_td2 = document.createElement('td')
            new_td2.textContent = store.store.Type

            const new_td3 = document.createElement('td')
            new_td3.textContent = store.store.Address

            new_tb_tr.appendChild(new_td1)
            new_tb_tr.appendChild(new_td2)
            new_tb_tr.appendChild(new_td3)
            store_table.appendChild(new_tb_tr)

        })
}

function get_store_month_revenue_by_id() {
    
    const id = get_url_by_id();

    fetch(`/api/store/info/month/revenue/${id}`)
        .then(response => response.json())
        .then(store_revenues => {
            // console.log(store_revenues.store_revenues)

            const revenueResultDiv = document.getElementById('store_revenue');
            revenueResultDiv.innerHTML = ""; // 기존 데이터 제거

            const new_p = document.createElement('p')
            new_p.textContent = "월간 매출액"

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'revenue_table');
            const new_th_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "MONTH"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "REVENUE"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "COUNT"

            new_th_tr.appendChild(new_th1)
            new_th_tr.appendChild(new_th2)
            new_th_tr.appendChild(new_th3)
            new_table.appendChild(new_th_tr)
            revenueResultDiv.appendChild(new_p)
            revenueResultDiv.appendChild(new_table)

            store_revenues.store_revenues.forEach(store_revenue => {
                
                const revenue_table = document.getElementById('revenue_table');
                const new_tb_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                const td1_a = document.createElement('a')
                td1_a.setAttribute('href', `/api/store/info/day/revenue/${store_revenue.Id}?month=${store_revenue.Month}`)
                td1_a.textContent = store_revenue.Month

                const new_td2 = document.createElement('td')
                new_td2.textContent = store_revenue.Revenue

                const new_td3 = document.createElement('td')
                new_td3.textContent = store_revenue.Count

                new_td1.appendChild(td1_a)
                new_tb_tr.appendChild(new_td1)
                new_tb_tr.appendChild(new_td2)
                new_tb_tr.appendChild(new_td3)
                revenue_table.appendChild(new_tb_tr)
                
            });

        })
}

function get_store_day_revenue_by_month(month) {

    const id = get_url_by_id();

    fetch(`/api/store/info/day/revenue/${id}?month=${month}`)
        .then(response => response.json())
        .then(store_revenues => {
            // console.log(store_revenues.store_revenues)

            const revenueResultDiv = document.getElementById('store_revenue');
            revenueResultDiv.innerHTML = ""; // 기존 데이터 제거

            const back = document.createElement('a')
            back.setAttribute('href', `/api/store/${id}`)
            back.setAttribute('class', 'back-button')
            back.textContent = "월간 매출액 보기"

            const new_p = document.createElement('p')
            new_p.textContent = "일간 매출액"

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'revenue_table');
            const new_th_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "MONTH"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "REVENUE"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "COUNT"

            new_th_tr.appendChild(new_th1)
            new_th_tr.appendChild(new_th2)
            new_th_tr.appendChild(new_th3)
            new_table.appendChild(new_th_tr)
            revenueResultDiv.appendChild(new_p)
            revenueResultDiv.appendChild(back)
            revenueResultDiv.appendChild(new_table)

            store_revenues.store_revenues.forEach(store_revenue => {
                
                const revenue_table = document.getElementById('revenue_table');
                const new_tb_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                new_td1.textContent = store_revenue.Month

                const new_td2 = document.createElement('td')
                new_td2.textContent = store_revenue.Revenue

                const new_td3 = document.createElement('td')
                new_td3.textContent = store_revenue.Count

                new_tb_tr.appendChild(new_td1)
                new_tb_tr.appendChild(new_td2)
                new_tb_tr.appendChild(new_td3)
                revenue_table.appendChild(new_tb_tr)
                
            });

        })
}

function get_user_by_user_id() {
    const id = get_url_by_id();

    fetch(`/api/store/info/user/${id}`)
        .then(response => response.json())
        .then(users => {
            // console.log(users.users)

            const userResultDiv = document.getElementById('user_result');
            userResultDiv.innerHTML = ""; // 기존 데이터 제거

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'user_table');
            const new_th_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "USER_ID"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "NAME"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "FREQUENCY"

            new_th_tr.appendChild(new_th1)
            new_th_tr.appendChild(new_th2)
            new_th_tr.appendChild(new_th3)
            new_table.appendChild(new_th_tr)
            userResultDiv.appendChild(new_table)

            users.users.forEach(user => {

                const user_table = document.getElementById('user_table');
                const new_tb_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                const td1_a = document.createElement('a')
                td1_a.setAttribute('href', `/api/user/${user.Id}`)
                td1_a.textContent = user.Id

                const new_td2 = document.createElement('td')
                new_td2.textContent = user.Name

                const new_td3 = document.createElement('td')
                new_td3.textContent = user.Count

                new_td1.appendChild(td1_a)
                new_tb_tr.appendChild(new_td1)
                new_tb_tr.appendChild(new_td2)
                new_tb_tr.appendChild(new_td3)
                user_table.appendChild(new_tb_tr)

            })
        })
}

document.addEventListener('DOMContentLoaded', () => {
    get_store_by_id()
    get_store_month_revenue_by_id()
    get_user_by_user_id()
})

document.getElementById('store_revenue').addEventListener('click', (e) => {
    
    if (e.target.tagName === 'A') {
        const href = e.target.getAttribute('href')

        // a 태그의 href에서 ? 를 기준으로 나눠서 ? 뒤의 값 중 month를 추출
        if (href.includes('?month=')) {
            e.preventDefault()
            const urlParams = new URLSearchParams(href.split('?')[1])
            const month = urlParams.get('month')

            get_store_day_revenue_by_month(month)
        }

    }

})
