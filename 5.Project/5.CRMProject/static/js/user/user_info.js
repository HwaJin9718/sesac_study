function get_url_by_id() {
    const url_path = window.location.pathname.split('/') // /를 기준으로 나눠서 url 파라미터 추출
    return url_path[url_path.length - 1] // 추출된 리스트의 마지막 값 리턴
}

function get_user_by_id() {

    const id = get_url_by_id();

    fetch(`/api/user/info/${id}`)
        .then(response => response.json())
        .then(user => {
            // console.log(user.user)

            const userResultDiv = document.getElementById('user_result');
            userResultDiv.innerHTML = ""; // 기존 데이터 제거

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'user_table');
            const new_th_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "NAME"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "GENDER"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "AGE"

            const new_th4 = document.createElement('th')
            new_th4.textContent = "BIRTHDAY"

            const new_th5 = document.createElement('th')
            new_th5.textContent = "ADDRESS"

            new_th_tr.appendChild(new_th1)
            new_th_tr.appendChild(new_th2)
            new_th_tr.appendChild(new_th3)
            new_th_tr.appendChild(new_th4)
            new_th_tr.appendChild(new_th5)
            new_table.appendChild(new_th_tr)
            userResultDiv.appendChild(new_table)

            const user_table = document.getElementById('user_table');
            const new_tb_tr = document.createElement('tr')

            const new_td1 = document.createElement('td')
            new_td1.textContent = user.user.Name

            const new_td2 = document.createElement('td')
            new_td2.textContent = user.user.Gender

            const new_td3 = document.createElement('td')
            new_td3.textContent = user.user.Age

            const new_td4 = document.createElement('td')
            new_td4.textContent = user.user.Birthdate

            const new_td5 = document.createElement('td')
            new_td5.textContent = user.user.Address

            new_tb_tr.appendChild(new_td1)
            new_tb_tr.appendChild(new_td2)
            new_tb_tr.appendChild(new_td3)
            new_tb_tr.appendChild(new_td4)
            new_tb_tr.appendChild(new_td5)
            user_table.appendChild(new_tb_tr)

        })
}

function get_order_by_user_id() {
    const id = get_url_by_id();

    fetch(`/api/user/info/order/${id}`)
        .then(response => response.json())
        .then(orders => {
            // console.log(orders.orders)

            const orderResultDiv = document.getElementById('order_result');
            orderResultDiv.innerHTML = ""; // 기존 데이터 제거

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'order_table');
            const new_th_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "ORDER_ID"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "PURCHASED_DATE"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "PURCHASED_LOCATION"

            new_th_tr.appendChild(new_th1)
            new_th_tr.appendChild(new_th2)
            new_th_tr.appendChild(new_th3)
            new_table.appendChild(new_th_tr)
            orderResultDiv.appendChild(new_table)

            orders.orders.forEach(order => {

                const order_table = document.getElementById('order_table');
                const new_tb_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                const td1_a = document.createElement('a')
                td1_a.setAttribute('href', `/api/order_item/${order.Id}`)
                td1_a.textContent = order.Id

                const new_td2 = document.createElement('td')
                new_td2.textContent = order.OrderAt

                const new_td3 = document.createElement('td')
                const td3_a = document.createElement('a')
                td3_a.setAttribute('href', `/api/store/${order.StoreId}`)
                td3_a.textContent = order.StoreId

                new_td1.appendChild(td1_a)
                new_td3.appendChild(td3_a)
                new_tb_tr.appendChild(new_td1)
                new_tb_tr.appendChild(new_td2)
                new_tb_tr.appendChild(new_td3)
                order_table.appendChild(new_tb_tr)

            });

        })
}

function get_store_by_user_id() {
    const id = get_url_by_id();

    fetch(`/api/user/info/store/${id}`)
        .then(response => response.json())
        .then(stores => {
            // console.log(stores.stores)
            stores.stores.forEach(store => {
                // console.log(store)
                const storeResultDiv = document.getElementById('store_result');

                const new_ul = document.createElement('ul')
                const new_li = document.createElement('li')
                new_li.textContent = `${store.Name} (${store.Count}번 방문)`

                new_ul.appendChild(new_li)
                storeResultDiv.appendChild(new_ul)
            })
        })
}

function get_item_by_user_id() {
    const id = get_url_by_id();

    fetch(`/api/user/info/item/${id}`)
        .then(response => response.json())
        .then(items => {
            console.log(items.items)
            items.items.forEach(item => {
                // console.log(item)
                const itemResultDiv = document.getElementById('item_result');

                const new_ul = document.createElement('ul')
                const new_li = document.createElement('li')
                new_li.textContent = `${item.Name} (${item.Count}번 주문)`

                new_ul.appendChild(new_li)
                itemResultDiv.appendChild(new_ul)
            })
        })
}

document.addEventListener('DOMContentLoaded', () => {
    get_user_by_id()
    get_order_by_user_id()
    get_store_by_user_id()
    get_item_by_user_id()
})
