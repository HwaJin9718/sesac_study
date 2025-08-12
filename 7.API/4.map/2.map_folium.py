# pip install folium
import folium

# 63빌딩의 위도와 경도
# latitude = 37.5193
# longitude = 126.9408

# # folium 맵 객체 생성
# m = folium.Map(location=[latitude, longitude], zoom_start=16)

# # 63빌딩 위치에 마커 추가
# folium.Marker([latitude, longitude], popup='63 Building').add_to(m)

# # 맵 저장 및 출력
# m.save("63-building-map.html") # 해당 코드가 실행되면 63-building-map.html 파일이 생성됨

# ==================================================
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def map_view():
    latitude, longitude = 37.5193, 126.9408  # Default to 63 Building
    if request.method == 'POST':
        latitude = float(request.form.get('latitude', latitude))
        longitude = float(request.form.get('longitude', longitude))

    # Create folium map
    folium_map = folium.Map(location=[latitude, longitude], zoom_start=16)
    folium.Marker([latitude, longitude], popup='Location').add_to(folium_map)

    # Render map to HTML
    map_html = folium_map._repr_html_()
    return render_template('map.html', latitude=latitude, longitude=longitude, map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)
