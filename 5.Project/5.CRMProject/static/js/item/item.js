// 공통 페이징 함수
function createPagination(currentPage, totalPages, baseUrl, queryString = '') {
    const pageDiv = document.getElementById('paging');
    pageDiv.innerHTML = ""; // 기존 데이터 제거
    
    if (totalPages <= 1) {
        // pageDiv.remove(); // 페이지가 1개 이하면 페이징 안함
        pageDiv.style.display = 'none'; // 페이지 태그 안보이도록 함
        return
    }
    
    const query = queryString ? `?${queryString}` : '';
    
    // Previous 버튼
    if (currentPage > 1) {
        const previous = document.createElement('a');
        previous.setAttribute('href', `${baseUrl}/${currentPage - 1}${query}`);
        previous.textContent = "Previous";
        pageDiv.appendChild(previous);
    }
    
    // 페이지 번호
    const pages = getPageNumbers(currentPage, totalPages);
    
    pages.forEach((page, index) => {
        if (page === '...') {
            const ellipsis = document.createElement('span');
            ellipsis.className = 'ellipsis';
            ellipsis.textContent = '...';
            pageDiv.appendChild(ellipsis);
        } else {
            const a = document.createElement('a');
            a.setAttribute('href', `${baseUrl}/${page}${query}`);
            a.textContent = page;
            
            if (page == currentPage) {
                a.className = 'current';
            }
            
            pageDiv.appendChild(a);
        }
    });
    
    // Next 버튼
    if (currentPage < totalPages) {
        const next = document.createElement('a');
        next.setAttribute('href', `${baseUrl}/${parseInt(currentPage) + 1}${query}`);
        next.textContent = "Next";
        pageDiv.appendChild(next);
    }
}

// 페이지 번호 배열 생성 함수
function getPageNumbers(currentPage, totalPages) {
    const pages = [];
    const current = parseInt(currentPage);
    const total = parseInt(totalPages);
    
    if (total <= 7) {
        // 페이지가 7개 이하면 모든 페이지 표시
        for (let i = 1; i <= total; i++) {
            pages.push(i);
        }
    } else {
        // 첫 페이지는 항상 표시
        pages.push(1);
        
        let startPage, endPage;
        
        if (current <= 4) {
            // 현재 페이지가 앞쪽에 있을 때
            startPage = 2;
            endPage = 5;
        } else if (current >= total - 3) {
            // 현재 페이지가 뒤쪽에 있을 때
            startPage = total - 4;
            endPage = total - 1;
        } else {
            // 현재 페이지가 중간에 있을 때
            startPage = current - 1;
            endPage = current + 1;
        }
        
        // 첫 페이지와 시작 페이지 사이에 gap이 있으면 ... 추가
        if (startPage > 2) {
            pages.push('...');
        }
        
        // 중간 페이지들 추가
        for (let i = startPage; i <= endPage; i++) {
            if (i > 1 && i < total) {
                pages.push(i);
            }
        }
        
        // 끝 페이지와 마지막 페이지 사이에 gap이 있으면 ... 추가
        if (endPage < total - 1) {
            pages.push('...');
        }
        
        // 마지막 페이지는 항상 표시
        pages.push(total);
    }
    
    return pages;
}

function get_page_by_url() {
    // url 파라미터 확인
    const url_path = window.location.pathname.split('/') // /를 기준으로 나눠서 url 파라미터 추출

    // 검색(search) 페이지 여부 확인
    if (url_path.includes('search')) {
        return {
            type : 'search',
            page : url_path[url_path.length - 1] // || 1 추출된 리스트의 마지막 값 (현재 페이지) 리턴
        }
    }

    let page_num = 0

    if (url_path[url_path.length - 1] == 0) {
        page_num = 1
    } else {
        page_num = url_path[url_path.length - 1] 
    }
    
    return {
        type : 'normal',
        page : page_num
    }
    
}

function get_search_param() {
    const params = new URLSearchParams(window.location.search)
    const type = params.get('type')

    return {
        // 삼항 연산자 처리
        type: type === "null" || type === null ? null : type
    }
    
}

function get_items() {
    const url = get_page_by_url()
    fetch('/api/item/data')
        .then(response => response.json())
        .then(items => {
            const resultDiv = document.getElementById('result');
            const pageDiv = document.getElementById('paging');
            resultDiv.innerHTML = ""; // 기존 데이터 제거
            pageDiv.innerHTML = ""; // 기존 데이터 제거

            if (items.items.length === 0) {
                const new_p = document.createElement('p')
                new_p.textContent = "검색 결과가 없습니다."
                resultDiv.appendChild(new_p)
                return;
            }

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'item_table');
            const new_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "ID"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "TYPE"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "NAME"

            const new_th4 = document.createElement('th')
            new_th4.textContent = "UNIT_PRICE"

            new_tr.appendChild(new_th1)
            new_tr.appendChild(new_th2)
            new_tr.appendChild(new_th3)
            new_tr.appendChild(new_th4)
            new_table.appendChild(new_tr)
            resultDiv.appendChild(new_table)
        
            items.items.forEach(item => {

                const item_table = document.getElementById('item_table');
                const new_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                
                const td1_a = document.createElement('a')
                td1_a.setAttribute('href', `/api/item/${item.Id}`)
                td1_a.textContent = item.Id

                const new_td2 = document.createElement('td')
                new_td2.textContent = item.Type

                const new_td3 = document.createElement('td')
                new_td3.textContent = item.Name

                const new_td4 = document.createElement('td')
                new_td4.textContent = item.UnitPrice

                new_td1.appendChild(td1_a)
                new_tr.appendChild(new_td1)
                new_tr.appendChild(new_td2)
                new_tr.appendChild(new_td3)
                new_tr.appendChild(new_td4)
                item_table.appendChild(new_tr)

            });

            // 페이징 함수
            createPagination(url.page, items.total_page, '/api/item')
            
            });
}

function get_items_by_page() {
    const url = get_page_by_url()
    fetch(`/api/item/page/data/${url.page}`)
        .then(response => response.json())
        .then(items => {
            const resultDiv = document.getElementById('result');
            const pageDiv = document.getElementById('paging');
            resultDiv.innerHTML = ""; // 기존 데이터 제거
            pageDiv.innerHTML = ""; // 기존 데이터 제거

            if (items.items.length === 0) {
                const new_p = document.createElement('p')
                new_p.textContent = "검색 결과가 없습니다."
                resultDiv.appendChild(new_p)
                return;
            }

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'item_table');
            const new_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "ID"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "TYPE"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "NAME"

            const new_th4 = document.createElement('th')
            new_th4.textContent = "UNIT_PRICE"

            new_tr.appendChild(new_th1)
            new_tr.appendChild(new_th2)
            new_tr.appendChild(new_th3)
            new_tr.appendChild(new_th4)
            new_table.appendChild(new_tr)
            resultDiv.appendChild(new_table)
        
            items.items.forEach(item => {

                const item_table = document.getElementById('item_table');
                const new_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                
                const td1_a = document.createElement('a')
                td1_a.setAttribute('href', `/api/item/${item.Id}`)
                td1_a.textContent = item.Id

                const new_td2 = document.createElement('td')
                new_td2.textContent = item.Type

                const new_td3 = document.createElement('td')
                new_td3.textContent = item.Name

                const new_td4 = document.createElement('td')
                new_td4.textContent = item.UnitPrice

                new_td1.appendChild(td1_a)
                new_tr.appendChild(new_td1)
                new_tr.appendChild(new_td2)
                new_tr.appendChild(new_td3)
                new_tr.appendChild(new_td4)
                item_table.appendChild(new_tr)

            });

            // 페이징 함수
            createPagination(url.page, items.total_page, '/api/item')
            
            });
}

function search_items() {
    const url = get_page_by_url()

    const type = document.querySelector('select[name="type"]').value.trim();
    // console.log('검색된 type', type)

    if (!type) {
        // 검색값이 없으면 일반 조회 페이지로 리다이렉트
        window.location.href = '/api/item/1';
        return;
    }

    fetch(`/api/item/search?type=${type}`)
        .then(response => response.json())
        .then(items => {
            // console.log(items.items)
            // console.log(items.total_page)
            const resultDiv = document.getElementById('result');
            const pageDiv = document.getElementById('paging');
            resultDiv.innerHTML = ""; // 기존 데이터 제거
            pageDiv.innerHTML = ""; // 기존 데이터 제거

            if (items.items.length === 0) {
                const new_p = document.createElement('p')
                new_p.textContent = "검색 결과가 없습니다."
                resultDiv.appendChild(new_p)
                return;
            }

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'item_table');
            const new_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "ID"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "TYPE"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "NAME"

            const new_th4 = document.createElement('th')
            new_th4.textContent = "UNIT_PRICE"

            new_tr.appendChild(new_th1)
            new_tr.appendChild(new_th2)
            new_tr.appendChild(new_th3)
            new_tr.appendChild(new_th4)
            new_table.appendChild(new_tr)
            resultDiv.appendChild(new_table)
        
            items.items.forEach(item => {

                const item_table = document.getElementById('item_table');
                const new_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                
                const td1_a = document.createElement('a')
                td1_a.setAttribute('href', `/api/item/${item.Id}`)
                td1_a.textContent = item.Id

                const new_td2 = document.createElement('td')
                new_td2.textContent = item.Type

                const new_td3 = document.createElement('td')
                new_td3.textContent = item.Name

                const new_td4 = document.createElement('td')
                new_td4.textContent = item.UnitPrice

                new_td1.appendChild(td1_a)
                new_tr.appendChild(new_td1)
                new_tr.appendChild(new_td2)
                new_tr.appendChild(new_td3)
                new_tr.appendChild(new_td4)
                item_table.appendChild(new_tr)

            });

            // 쿼리 스트링 생성
            const queryParam = new URLSearchParams();
            if (type) {
                queryParam.append('type', type)
            }
            const queryString = queryParam.toString();

            // 페이징 함수
            createPagination(1, items.total_page, '/api/item/search', queryString)
        })
}

function search_items_paging() {
    const url = get_page_by_url()

    // 쿼리 스트링 생성
    const searchParams = get_search_param()

    if (!searchParams) {
        get_items_by_page()
        return;
    }

    // null이나 빈 값 필터링
    const filteredParams = new URLSearchParams();

    if (searchParams.type && searchParams.type !== "null") {
        filteredParams.append('type', searchParams.type)
    }

    const queryString = filteredParams.toString();

    fetch(`/api/item/search/page/${url.page}?${queryString}`)
        .then(response => response.json())
        .then(items => {
            const resultDiv = document.getElementById('result');
            const pageDiv = document.getElementById('paging');
            resultDiv.innerHTML = ""; // 기존 데이터 제거
            pageDiv.innerHTML = ""; // 기존 데이터 제거

            if (items.items.length === 0) {
                const new_p = document.createElement('p')
                new_p.textContent = "검색 결과가 없습니다."
                resultDiv.appendChild(new_p)
                return;
            }

            const type = document.getElementById('type')
            type.setAttribute('value', items.search_name)

            const new_table = document.createElement('table');
            new_table.setAttribute('id', 'item_table');
            const new_tr = document.createElement('tr')

            const new_th1 = document.createElement('th')
            new_th1.textContent = "ID"

            const new_th2 = document.createElement('th')
            new_th2.textContent = "TYPE"

            const new_th3 = document.createElement('th')
            new_th3.textContent = "NAME"

            const new_th4 = document.createElement('th')
            new_th4.textContent = "UNIT_PRICE"

            new_tr.appendChild(new_th1)
            new_tr.appendChild(new_th2)
            new_tr.appendChild(new_th3)
            new_tr.appendChild(new_th4)
            new_table.appendChild(new_tr)
            resultDiv.appendChild(new_table)
        
            items.items.forEach(item => {

                const item_table = document.getElementById('item_table');
                const new_tr = document.createElement('tr')

                const new_td1 = document.createElement('td')
                
                const td1_a = document.createElement('a')
                td1_a.setAttribute('href', `/api/item/${item.Id}`)
                td1_a.textContent = item.Id

                const new_td2 = document.createElement('td')
                new_td2.textContent = item.Type

                const new_td3 = document.createElement('td')
                new_td3.textContent = item.Name

                const new_td4 = document.createElement('td')
                new_td4.textContent = item.UnitPrice

                new_td1.appendChild(td1_a)
                new_tr.appendChild(new_td1)
                new_tr.appendChild(new_td2)
                new_tr.appendChild(new_td3)
                new_tr.appendChild(new_td4)
                item_table.appendChild(new_tr)

            });

            // 페이징 함수
            createPagination(url.page, items.total_page, '/api/item/search', queryString)

        })
}

document.addEventListener('DOMContentLoaded', () => {
    const url = get_page_by_url()
    if (url.type === 'search') {
        search_items_paging()
    } else if (url.page == 1) {
        get_items()
    } else {
        get_items_by_page()
    }
})

document.getElementById('search_form').addEventListener('submit', (e) => {
    e.preventDefault();
    search_items()
})
