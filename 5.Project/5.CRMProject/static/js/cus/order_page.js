function get_store_type() {
    fetch('/api/cus/orderpage/type')
        .then(response => response.json())
        .then(types => {
            // console.log(types)
            const select = document.getElementById('type')
            const option = document.createElement('option')
            option.textContent = '선택하세요'
            select.appendChild(option)

            types.types.forEach(type => {
                const option = document.createElement('option')
                option.setAttribute('value', type.Type)
                option.textContent = type.Type
                select.appendChild(option)
            });

        })
}

function get_store_name(type) {
    fetch(`/api/cus/orderpage/name/${type}`)
        .then(response => response.json())
        .then(names => {
            // console.log(names.names)

            const search = document.getElementById('search_form')
            const label = document.createElement('label')
            label.setAttribute('for', 'name')
            label.textContent = '주문 매장 선택'

            const select = document.createElement('select')
            select.setAttribute('name', 'name')
            select.setAttribute('id', 'name')

            const option = document.createElement('option')
            option.textContent = '선택하세요'

            select.appendChild(option)
            search.appendChild(label)
            search.appendChild(select)

            names.names.forEach(name => {
                const option = document.createElement('option')
                option.setAttribute('value', name.Id)
                option.textContent = name.Name
                select.appendChild(option)
            })
        })
}

function get_item(store_id) {
    fetch('/api/cus/orderpage/item')
        .then(response => response.json())
        .then(items => {
            // console.log(items.items)

            // 기존 result div 제거
            const existingResult = document.getElementById('result');
            if (existingResult) {
                existingResult.remove();
            }

            const body = document.body;
            const div = document.createElement('div')
            div.setAttribute('id', 'result')
            body.appendChild(div)

            const resultDiv = document.getElementById('result');

            const order_form = document.createElement('form');
            order_form.setAttribute('id', 'order_form')

            resultDiv.appendChild(order_form)

            const form = document.getElementById('order_form');

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'item_table');
            const new_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')

            const new_th2 = document.createElement('th')
            new_th2.textContent = "NAME"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "PRICE"

            new_tr.appendChild(new_th1)
            new_tr.appendChild(new_th2)
            new_tr.appendChild(new_th3)
            new_table.appendChild(new_tr)
            form.appendChild(new_table)

            items.items.forEach(item => {
                // console.log(item)

                const item_table = document.getElementById('item_table');
                const new_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                const td1_input = document.createElement('input')
                td1_input.setAttribute('type', 'checkbox')
                td1_input.setAttribute('name', 'item')
                td1_input.setAttribute('value', item.Id)

                const new_td2 = document.createElement('td')
                new_td2.textContent = item.Name

                const new_td3 = document.createElement('td')
                new_td3.textContent = item.UnitPrice

                new_td1.appendChild(td1_input)
                new_tr.appendChild(new_td1)
                new_tr.appendChild(new_td2)
                new_tr.appendChild(new_td3)
                item_table.appendChild(new_tr)

            });

            const storeId = document.createElement('input');
            storeId.setAttribute('type', 'hidden');
            storeId.setAttribute('name', 'store_id');
            storeId.setAttribute('value', store_id);
            form.appendChild(storeId);

            const btn = document.createElement('button');
            btn.setAttribute('type', 'submit')
            btn.setAttribute('class', 'back-button')
            btn.textContent = '주문하기'
            form.appendChild(btn)

        })
}

function crate_order() {

    const checkedBoxes = document.querySelectorAll('input[name="item"]:checked');
    const checkedItems = Array.from(checkedBoxes).map(cb => cb.value);
    // console.log('선택된 상품:', checkedItems);

    const store_id = document.querySelector('input[name="store_id"]').value;
    // console.log('매장 ID:', storeId);

    const user = JSON.parse(sessionStorage.getItem('user'));
    // console.log(user)

    const formData = new FormData();
    formData.append('user_id', user.Id);
    formData.append('store_id', store_id);
    checkedItems.forEach(item => {
        // console.log(item)
        formData.append('items', item);
    })

    fetch(`/api/cus/orderpage/order`, {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(create_result => {
            console.log(create_result.create_result)
            if (create_result.create_result === true) {
                alert('주문이 완료되었습니다.');
                window.location.href = '/api/cus';
            } else {
                alert('주문이 실패하였습니다.');
                window.location.href = '/api/cus';
            }
        })
}

document.addEventListener('DOMContentLoaded', () => {
    get_store_type()

    document.addEventListener('submit', (e) => {
        if (e.target.id === 'order_form') {
            e.preventDefault(); // form의 기본 submit 동작 방지
            crate_order()
        }
    })
})

// change 이벤트
document.addEventListener('change', function(e) {
    if (e.target.id === 'type') {
        // type 변경 시
        const selectedType = e.target.value;
        get_store_name(selectedType)
    } else if (e.target.id === 'name') {
        // name 변경 시
        const selectedNameId = e.target.value;
        get_item(selectedNameId)
    }
})
