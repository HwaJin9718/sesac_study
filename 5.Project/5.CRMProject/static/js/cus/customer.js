// hello 에 고객 이름 추가해주기
// 기본적으로 고객 주문 목록 보여줘야 함, 없으면 주문 목록이 없습니다 나오야 함
    function get_user_name_and_id() {
    const name = document.getElementById('hello')

    // login 페이지에서 sessionStorage로 전달한 user 정보를 받아옴
    const user = JSON.parse(sessionStorage.getItem('user'));

    name.textContent = `안녕하세요! ${user.Name} 고객님`
    }

    function get_orders() {
    const user = JSON.parse(sessionStorage.getItem('user'));
    
    fetch(`/api/cus/order/${user.Id}`)
        .then(response => response.json())
        .then(orders => {
            // console.log(orders);

            const resultDiv = document.getElementById('result')
            resultDiv.innerHTML = ""; // 기존 데이터 제거

            if (orders.orders.length === 0) {
                const new_p = document.createElement('p')
                new_p.textContent = "주문 내역이 없습니다."
                resultDiv.appendChild(new_p)
                return;
            }

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'order_table');
            const new_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "STORE_NAME"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "ORDER_AT"

            const new_th3 = document.createElement('th')

            new_tr.appendChild(new_th1)
            new_tr.appendChild(new_th2)
            new_tr.appendChild(new_th3)
            new_table.appendChild(new_tr)
            resultDiv.appendChild(new_table)

            orders.orders.forEach(order => {

                const order_table = document.getElementById('order_table');
                const new_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                new_td1.textContent = order.StoreName

                const new_td2 = document.createElement('td')
                new_td2.textContent = order.OrderAt
                
                const new_td3 = document.createElement('td')
                
                const td3_a = document.createElement('a')
                td3_a.setAttribute('href', `/api/cus/order/${user.Id}/${order.OrderAt}`)
                td3_a.setAttribute('class', 'order-detail')
                td3_a.textContent = '주문 상품 보러가기'

                new_td3.appendChild(td3_a)
                new_tr.appendChild(new_td1)
                new_tr.appendChild(new_td2)
                new_tr.appendChild(new_td3)
                order_table.appendChild(new_tr)

            });
            
        })

    }

    function get_order_item(user_id, order_at) {
    fetch(`/api/cus/order/${user_id}/${order_at}`)
        .then(response => response.json())
        .then(items => {
            // console.log(items)
            // console.log(items[0].OrderAt)

            const resultDiv = document.getElementById('result')
            resultDiv.innerHTML = ""; // 기존 데이터 제거

            const new_p = document.createElement('p')
            new_p.textContent = `주문 일시 : ${items.items[0].OrderAt}`

            const back = document.createElement('a')
            back.setAttribute('href', `/api/cus/`)
            back.setAttribute('class', 'back-button')
            back.textContent = "주문 목록 보기"

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'item_table');
            const new_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "ITEM_NAME"

            resultDiv.appendChild(new_p)
            resultDiv.appendChild(back)
            new_tr.appendChild(new_th1)
            new_table.appendChild(new_tr)
            resultDiv.appendChild(new_table)

            items.items.forEach(item => {

                const item_table = document.getElementById('item_table');
                const new_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                new_td1.textContent = item.ItemName

                new_tr.appendChild(new_td1)
                item_table.appendChild(new_tr)

            });

        })

    }

document.addEventListener('DOMContentLoaded', () => {
    get_user_name_and_id()
    get_orders()
})

document.getElementById('result').addEventListener('click', (e) => {
    
    if (e.target.tagName === 'A' && e.target.classList.contains('order-detail')) {
        const href = e.target.getAttribute('href')

        // a 태그의 href에서 / 를 기준으로 나눠서 user_id 와 order_at 추출
        if (href.includes('/')) {
            e.preventDefault()
            const path = href.split('/');
            const user_id = path[path.length - 2];
            const order_at = path[path.length - 1];

            get_order_item(user_id, order_at)
        }

    }

})
