function get_url_by_id() {
    const url_path = window.location.pathname.split('/') // /를 기준으로 나눠서 url 파라미터 추출
    return url_path[url_path.length - 1] // 추출된 리스트의 마지막 값 리턴
}

function get_item_by_id() {

    const id = get_url_by_id();

    fetch(`/api/item/info/${id}`)
        .then(response => response.json())
        .then(item => {

            const itemResultDiv = document.getElementById('item_result');
            itemResultDiv.innerHTML = ""; // 기존 데이터 제거

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'item_table');
            const new_th_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "NAME"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "UNIT_PRICE"

            new_th_tr.appendChild(new_th1)
            new_th_tr.appendChild(new_th2)
            new_table.appendChild(new_th_tr)
            itemResultDiv.appendChild(new_table)

            const item_table = document.getElementById('item_table');
            const new_tb_tr = document.createElement('tr')

            const new_td1 = document.createElement('td')
            new_td1.textContent = item.item.Name

            const new_td2 = document.createElement('td')
            new_td2.textContent = item.item.UnitPrice

            new_tb_tr.appendChild(new_td1)
            new_tb_tr.appendChild(new_td2)
            item_table.appendChild(new_tb_tr)

        })
}

function get_item_month_revenue_by_id() {
    
    const id = get_url_by_id();

    fetch(`/api/item/info/month/revenue/${id}`)
        .then(response => response.json())
        .then(item_revenues => {
            // console.log(item_revenues.item_revenues)

            const revenueResultDiv = document.getElementById('item_revenue');
            revenueResultDiv.innerHTML = ""; // 기존 데이터 제거

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'revenue_table');
            const new_th_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "MONTH"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "TOTAL_REVENUE"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "ITEM_COUNT"

            new_th_tr.appendChild(new_th1)
            new_th_tr.appendChild(new_th2)
            new_th_tr.appendChild(new_th3)
            new_table.appendChild(new_th_tr)
            revenueResultDiv.appendChild(new_table)

            item_revenues.item_revenues.forEach(item_revenue => {
                
                const revenue_table = document.getElementById('revenue_table');
                const new_tb_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                new_td1.textContent = item_revenue.Month

                const new_td2 = document.createElement('td')
                new_td2.textContent = item_revenue.Revenue

                const new_td3 = document.createElement('td')
                new_td3.textContent = item_revenue.Count

                new_tb_tr.appendChild(new_td1)
                new_tb_tr.appendChild(new_td2)
                new_tb_tr.appendChild(new_td3)
                revenue_table.appendChild(new_tb_tr)
                
            });

        })
}

function get_chart_data() {

    const id = get_url_by_id();

    fetch(`/api/item/info/month/revenue/${id}`)
        .then(response => response.json())
        .then(item_revenues => {
            // console.log(item_revenues.item_revenues)
            draw_chart(item_revenues.item_revenues)
        })
}

function draw_chart(item_revenues) {
    // console.log(item_revenues)

    month = []
    item_revenues.forEach(item_revenue => {
        month.push(item_revenue.Month)
    })

    line_data = []
    item_revenues.forEach(item_revenue => {
        line_data.push(item_revenue.Revenue)
    })

    bar_data = []
    item_revenues.forEach(item_revenue => {
        bar_data.push(item_revenue.Count)
    })

    const ctx = document.getElementById('month_revenue');
    const labels = month
    const data = {
        labels: labels,
        datasets: [{
            label: 'Total Revenue',
            data: line_data,
            fill: false,
            borderColor: 'rgb(0, 161, 139)',
            backgroundColor: 'rgb(0, 161, 139)',
            tension: 0.1,
            type: 'line', // line 차트 지정
            yAxisID: 'y' // 왼쪽 Y축 사용
        }, {
            label: 'Item Count',
            data: bar_data,
            backgroundColor: 'rgba(0, 196, 170, 0.3)',
            borderColor: 'rgb(0, 196, 170)',
            borderWidth: 1,
            type: 'bar', // bar 차트 지정
            yAxisID: 'y1' // 오른쪽 Y축 사용
        }]
    }

    const config = {
        type: 'bar',
        data: data,
        options: {
            responsive: true, // 반응형 활성화
            maintainAspectRatio: false, // 비율 고정 해제
            scales: {
                y: {
                    beginAtZero: false,
                    position: 'left',
                    ticks: {
                        stepSize: 10000, // 10,000 단위로 눈금 표시
                    },
                    title: {
                        display: true,
                        text: '매출액',
                        font: {
                            size: 12,
                        }
                    }
                },
                y1: {
                    beginAtZero: true,
                    position: 'right',
                    title: {
                        display: true,
                        text: '판매개수',
                        font: {
                            size: 12,
                        }
                    }
                }
            },
            interaction: {
                mode: 'index', // x축 인덱스 기준으로 표시
                intersect: false // 정확한 포인트가 아니어도 표시
            },
            plugins: {
                tooltip: {
                    mode: 'index', // 툴팁도 인덱스 기준
                    intersect: false
                },
                legend: {
                    display: true,
                    position: 'bottom',
                    onClick: null // 범례 클릭 비활성화
                }
            }
        }
    };

    new Chart(ctx, config)

}

document.addEventListener('DOMContentLoaded', () => {
    get_item_by_id()
    get_item_month_revenue_by_id()
    get_chart_data()
})
