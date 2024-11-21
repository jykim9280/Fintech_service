import dash
from dash import html
import dash_bootstrap_components as dbc

# Dash 앱 초기화
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 앱 레이아웃
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                # 지도와 정보 패널을 Flexbox로 정렬
                html.Div(
                    style={
                        "display": "flex",
                        "flexDirection": "row",
                        "width": "100%",
                        "height": "600px",  # 전체 높이 설정
                    },
                    children=[
                        # 지도 영역
                        html.Div(
                            html.Iframe(
                                id="map",
                                srcDoc=f"""
                                <!DOCTYPE html>
                                <html>
                                <head>
                                    <meta charset="utf-8">
                                    <title>Kakao Map</title>
                                    <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=809f4e8d66fb1289847f037850859b15"></script>
                                    <style>
                                        body, html {{ margin: 0; padding: 0; width: 100%; height: 100%; }}
                                        #map {{ width: 100%; height: 100%; }}
                                    </style>
                                </head>
                                <body>
                                    <div id="map"></div>
                                    <script>
                                        var mapContainer = document.getElementById('map'); 
                                        var mapOption = {{ center: new kakao.maps.LatLng(37.4896557, 127.0328555), level: 4 }};
                                        var map = new kakao.maps.Map(mapContainer, mapOption);

                                        // 식당 데이터
                                        var restaurantData = [
                                            {{
                                                name: "뱅뱅막국수 역삼본점",
                                                type: "국수",
                                                rating: "4.4",
                                                phone: "0507-1392-4848",
                                                menu: "뱅뱅막국수, 들기름막국수, 육전",
                                                address: "서울 강남구 도곡로 112 서한빌딩 1층 103호",
                                                hours: "매일 11:00 ~ 21:00, 매일 휴게시간 15:00 ~ 16:30",
                                                lat: 37.4896557,
                                                lng: 127.0328555
                                            }},
                                            {{
                                                name: "서울식당 강남점",
                                                type: "한식",
                                                rating: "4.1",
                                                phone: "02-123-4567",
                                                menu: "김치찌개, 제육볶음",
                                                address: "서울 강남구 역삼동 123-45",
                                                hours: "매일 10:00 ~ 22:00",
                                                lat: 37.490565,
                                                lng: 127.034555
                                            }}
                                        ];

                                        // 마커 및 이벤트 설정
                                        restaurantData.forEach(function(restaurant) {{
                                            var marker = new kakao.maps.Marker({{
                                                position: new kakao.maps.LatLng(restaurant.lat, restaurant.lng),
                                                map: map
                                            }});

                                            kakao.maps.event.addListener(marker, 'click', function() {{
                                                var infoPanel = window.parent.document.getElementById('info-panel-content');
                                                infoPanel.innerHTML = `
                                                    <h4 style="margin-bottom: 10px;">${{restaurant.name}}</h4>
                                                    <p><b>업종:</b> ${{restaurant.type}}</p>
                                                    <p><b>평점:</b> ${{restaurant.rating}}</p>
                                                    <p><b>전화번호:</b> ${{restaurant.phone}}</p>
                                                    <p><b>대표 메뉴:</b> ${{restaurant.menu}}</p>
                                                    <p><b>주소:</b> ${{restaurant.address}}</p>
                                                    <p><b>영업시간:</b> ${{restaurant.hours}}</p>
                                                `;
                                            }});
                                        }});
                                    </script>
                                </body>
                                </html>
                                """,
                                style={"width": "100%", "height": "100%", "border": "none"},
                            ),
                            style={"flex": "2", "borderRight": "1px solid #ccc"},  # 지도의 너비 설정
                        ),
                        # 정보 패널
                        html.Div(
                            [
                                # 서비스 이름
                                html.H2(
                                    "찐뷰",
                                    style={
                                        "textAlign": "center",
                                        "marginBottom": "20px",
                                        "fontWeight": "bold",
                                    },
                                ),
                                # 기본 안내 문구
                                html.P(
                                    "마커를 클릭하세요.",
                                    style={
                                        "textAlign": "center",
                                        "fontSize": "16px",
                                        "color": "#555",
                                    },
                                ),
                                # 정보 표시 영역
                                html.Div(
                                    id="info-panel-content",
                                    style={
                                        "marginTop": "20px",
                                        "padding": "10px",
                                        "backgroundColor": "#fff",
                                        "border": "1px solid #ddd",
                                        "borderRadius": "5px",
                                        "boxShadow": "0 2px 5px rgba(0,0,0,0.1)",
                                    },
                                ),
                            ],
                            style={
                                "flex": "1",
                                "padding": "20px",
                                "overflowY": "auto",
                                "backgroundColor": "#f9f9f9",
                                "fontFamily": "Arial, sans-serif",
                            },
                        ),
                    ],
                ),
            ]
        )
    ],
    fluid=True,
)

# 앱 실행
if __name__ == "__main__":
    app.run_server(debug=True)
