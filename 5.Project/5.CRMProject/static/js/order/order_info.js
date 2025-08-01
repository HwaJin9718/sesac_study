function get_url_by_id() {
    const url_path = window.location.pathname.split('/') // /를 기준으로 나눠서 url 파라미터 추출
    return url_path[url_path.length - 1] // 추출된 리스트의 마지막 값 리턴
}

function get_order_by_id() {

    const id = get_url_by_id();

    fetch(`/api/order/info/${id}`)
        .then(response => response.json())
        .then(order => {

            const orderResultDiv = document.getElementById('order_result');
            orderResultDiv.innerHTML = ""; // 기존 데이터 제거

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'order_table');
            const new_th_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "ID"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "ORDERED_AT"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "STORE_ID"

            const new_th4 = document.createElement('th')
            new_th4.textContent = "USER_ID"

            new_th_tr.appendChild(new_th1)
            new_th_tr.appendChild(new_th2)
            new_th_tr.appendChild(new_th3)
            new_th_tr.appendChild(new_th4)
            new_table.appendChild(new_th_tr)
            orderResultDiv.appendChild(new_table)

            const order_table = document.getElementById('order_table');
            const new_tb_tr = document.createElement('tr')

            const new_td1 = document.createElement('td')
            new_td1.textContent = order.order.Id

            const new_td2 = document.createElement('td')
            new_td2.textContent = order.order.OrderAt

            const new_td3 = document.createElement('td')
            const td3_a = document.createElement('a')
            td3_a.setAttribute('href', `/api/store/${order.order.StoreId}`)
            td3_a.textContent = order.order.StoreId

            const new_td4 = document.createElement('td')
            const td4_a = document.createElement('a')
            td4_a.setAttribute('href', `/api/user/${order.order.UserId}`)
            td4_a.textContent = order.order.UserId

            new_td3.appendChild(td3_a)
            new_td4.appendChild(td4_a)
            new_tb_tr.appendChild(new_td1)
            new_tb_tr.appendChild(new_td2)
            new_tb_tr.appendChild(new_td3)
            new_tb_tr.appendChild(new_td4)
            order_table.appendChild(new_tb_tr)

        })
}

document.addEventListener('DOMContentLoaded', () => {
    get_order_by_id()
})
