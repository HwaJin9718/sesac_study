function get_url_by_id() {
    const url_path = window.location.pathname.split('/') // /를 기준으로 나눠서 url 파라미터 추출
    return url_path[url_path.length - 1] // 추출된 리스트의 마지막 값 리턴
}

function get_order_item_by_id() {

    const id = get_url_by_id();

    fetch(`/api/order_item/info/${id}`)
        .then(response => response.json())
        .then(order_items => {

            const orderItemResultDiv = document.getElementById('order_item_result');
            orderItemResultDiv.innerHTML = ""; // 기존 데이터 제거

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'order_item_table');
            const new_th_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "ID"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "ORDERED_ID"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "ITEM_ID"

            const new_th4 = document.createElement('th')
            new_th4.textContent = "ITEM_NAME"

            new_th_tr.appendChild(new_th1)
            new_th_tr.appendChild(new_th2)
            new_th_tr.appendChild(new_th3)
            new_th_tr.appendChild(new_th4)
            new_table.appendChild(new_th_tr)
            orderItemResultDiv.appendChild(new_table)

            order_items.order_items.forEach(order_item => {

                const order_item_table = document.getElementById('order_item_table');
                const new_tb_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                new_td1.textContent = order_item.Id

                const new_td2 = document.createElement('td')
                const td2_a = document.createElement('a')
                td2_a.setAttribute('href', `/api/order/${order_item.OrderId}`)
                td2_a.textContent = order_item.OrderId

                const new_td3 = document.createElement('td')
                const td3_a = document.createElement('a')
                td3_a.setAttribute('href', `/api/item/${order_item.ItemId}`)
                td3_a.textContent = order_item.ItemId

                const new_td4 = document.createElement('td')
                new_td4.textContent = order_item.Name

                new_td2.appendChild(td2_a)
                new_td3.appendChild(td3_a)
                new_tb_tr.appendChild(new_td1)
                new_tb_tr.appendChild(new_td2)
                new_tb_tr.appendChild(new_td3)
                new_tb_tr.appendChild(new_td4)
                order_item_table.appendChild(new_tb_tr)
                
            });

        })
}

document.addEventListener('DOMContentLoaded', () => {
    get_order_item_by_id()
})
