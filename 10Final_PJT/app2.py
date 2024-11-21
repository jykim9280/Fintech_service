# import dash
# from dash import html
# import dash_bootstrap_components as dbc

# # Dash 앱 초기화
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# # 앱 레이아웃
# app.layout = dbc.Container(
#     [
#         dbc.Row(
#             [
#                 # 지도와 정보 패널을 Flexbox로 정렬
#                 html.Div(
#                     style={
#                         "display": "flex",
#                         "flexDirection": "row",
#                         "width": "100%",
#                         "height": "100vh",  # 전체 높이 설정
#                     },
#                     children=[
#                         # 지도 영역
#                         html.Div(
#                             html.Iframe(
#                                 id="map",
#                                 srcDoc=f"""
#                                 <!DOCTYPE html>
#                                 <html>
#                                 <head>
#                                     <meta charset="utf-8">
#                                     <title>Kakao Map</title>
#                                     <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=809f4e8d66fb1289847f037850859b15"></script>
#                                     <style>
#                                         body, html {{ margin: 0; padding: 0; width: 100%; height: 100%; }}
#                                         #map {{ width: 100%; height: 100%; }}
#                                     </style>
#                                 </head>
#                                 <body>
#                                     <div id="map"></div>
#                                     <script>
#                                         var mapContainer = document.getElementById('map'); 
#                                         var mapOption = {{ center: new kakao.maps.LatLng(37.4896557, 127.0328555), level: 4 }};
#                                         var map = new kakao.maps.Map(mapContainer, mapOption);

#                                         // 반경 200m를 표시할 원의 중심 좌표
#                                         var centerPosition = new kakao.maps.LatLng(37.4896557, 127.0328555);

#                                         // 원 객체 생성
#                                         var circle = new kakao.maps.Circle({{
#                                             center: centerPosition,
#                                             radius: 200,  // 반경 200m
#                                             strokeWeight: 2,  // 선 두께
#                                             strokeColor: '#ff0000',  // 선 색상
#                                             strokeOpacity: 0.8,  // 선 투명도
#                                             strokeStyle: 'dashed',  // 선 스타일
#                                             fillColor: '#ffcccc',  // 채우기 색상
#                                             fillOpacity: 0.5  // 채우기 투명도
#                                         }});
#                                         circle.setMap(map);

#                                         // 마커 설정
#                                         var marker = new kakao.maps.Marker({{
#                                             position: centerPosition,
#                                             map: map
#                                         }});

#                                         kakao.maps.event.addListener(marker, 'click', function() {{
#                                             var infoPanel = window.parent.document.getElementById('info-panel-content');
#                                             infoPanel.innerHTML = `
#                                                 <div class="info-content">
#                                                     <h4>뱅뱅막국수 역삼본점</h4>
#                                                     <img src="https://via.placeholder.com/400" alt="뱅뱅막국수 역삼본점">
#                                                     <div class="details">
#                                                         <p><span class="label">업종:</span> 국수</p>
#                                                         <p><span class="label">평점:</span> ⭐ 4.4</p>
#                                                         <p><span class="label">전화번호:</span> 0507-1392-4848</p>
#                                                         <p><span class="label">대표 메뉴:</span> 뱅뱅막국수, 들기름막국수, 육전</p>
#                                                         <p><span class="label">주소:</span> 서울 강남구 도곡로 112 서한빌딩 1층 103호</p>
#                                                         <p><span class="label">영업시간:</span> 매일 11:00 ~ 21:00, 매일 휴게시간 15:00 ~ 16:30</p>
#                                                     </div>
#                                                 </div>
#                                             `;
#                                         }});
#                                     </script>
#                                 </body>
#                                 </html>
#                                 """,
#                                 style={"width": "100%", "height": "100%", "border": "none"},
#                             ),
#                             style={"flex": "2", "borderRight": "1px solid #ccc"},  # 지도의 너비 설정
#                         ),
#                         # 정보 패널
#                         html.Div(
#                             [
#                                 html.H2(
#                                     "찐뷰",
#                                     style={
#                                         "textAlign": "center",
#                                         "marginBottom": "20px",
#                                         "fontWeight": "bold",
#                                     },
#                                 ),
#                                 html.Div(
#                                     id="info-panel-content",
#                                     children="마커를 클릭하여 정보를 확인하세요.",
#                                     style={
#                                         "padding": "15px",
#                                         "backgroundColor": "#fff",
#                                         "border": "1px solid #ddd",
#                                         "borderRadius": "5px",
#                                         "boxShadow": "0 2px 5px rgba(0,0,0,0.1)",
#                                         "fontSize": "14px",
#                                         "lineHeight": "1.6",
#                                     },
#                                 ),
#                             ],
#                             style={
#                                 "flex": "1",
#                                 "padding": "20px",
#                                 "overflowY": "auto",
#                                 "backgroundColor": "#f9f9f9",
#                             },
#                         ),
#                     ],
#                 ),
#             ]
#         )
#     ],
#     fluid=True,
# )

# # 앱 실행
# if __name__ == "__main__":
#     app.run_server(debug=True)


# -------------------------11.20


import dash
from dash import html, Output, Input, dcc
import dash_bootstrap_components as dbc
import pandas as pd

# CSV 파일 로드
csv_path = 'C:/Fintech_service/10Final_PJT/뱅뱅막국수_combined_reviews.csv'
data = pd.read_csv(csv_path)

# Dash 앱 초기화
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 앱 레이아웃
app.layout = dbc.Container(
    [
        dcc.Store(id="marker-clicked", data=False),  # 마커 클릭 상태 저장
        dbc.Row(
            [
                # 지도와 정보 패널을 Flexbox로 정렬
                html.Div(
                    style={
                        "display": "flex",
                        "flexDirection": "row",
                        "width": "100%",
                        "height": "100vh",  # 전체 높이 설정
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

                                        // 반경 200m를 표시할 원의 중심 좌표
                                        var centerPosition = new kakao.maps.LatLng(37.4896557, 127.0328555);

                                        // 원 객체 생성
                                        var circle = new kakao.maps.Circle({{
                                            center: centerPosition,
                                            radius: 200,  // 반경 200m
                                            strokeWeight: 2,  // 선 두께
                                            strokeColor: '#ff0000',  // 선 색상
                                            strokeOpacity: 0.8,  // 선 투명도
                                            strokeStyle: 'dashed',  // 선 스타일
                                            fillColor: '#ffcccc',  // 채우기 색상
                                            fillOpacity: 0.5  // 채우기 투명도
                                        }});
                                        circle.setMap(map);

                                        // 마커 설정
                                        var marker = new kakao.maps.Marker({{
                                            position: centerPosition,
                                            map: map
                                        }});

                                        kakao.maps.event.addListener(marker, 'click', function() {{
                                            var infoPanel = window.parent.document.getElementById('info-panel-content');
                                            infoPanel.innerHTML = `
                                                <div class="info-content">
                                                    <h4>뱅뱅막국수 역삼본점</h4>
                                                    <img src="https://via.placeholder.com/400" alt="뱅뱅막국수 역삼본점">
                                                    <div class="details">
                                                        <p><span class="label">업종:</span> 국수</p>
                                                        <p><span class="label">평점:</span> ⭐ 4.4</p>
                                                        <p><span class="label">전화번호:</span> 0507-1392-4848</p>
                                                        <p><span class="label">대표 메뉴:</span> 뱅뱅막국수, 들기름막국수, 육전</p>
                                                        <p><span class="label">주소:</span> 서울 강남구 도곡로 112 서한빌딩 1층 103호</p>
                                                        <p><span class="label">영업시간:</span> 매일 11:00 ~ 21:00, 매일 휴게시간 15:00 ~ 16:30</p>
                                                    </div>
                                                </div>
                                            `;
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
                                html.H2(
                                    "찐뷰",
                                    style={
                                        "textAlign": "center",
                                        "marginBottom": "20px",
                                        "fontWeight": "bold",
                                    },
                                ),
                                html.Div(
                                    id="info-panel-content",
                                    children="마커를 클릭하여 정보를 확인하세요.",
                                    style={
                                        "padding": "15px",
                                        "backgroundColor": "#fff",
                                        "border": "1px solid #ddd",
                                        "borderRadius": "5px",
                                        "boxShadow": "0 2px 5px rgba(0,0,0,0.1)",
                                        "fontSize": "14px",
                                        "lineHeight": "1.6",
                                    },
                                ),
                                # "가성비" 버튼
                                html.Div(
                                    id="value-button-container",
                                    style={"marginTop": "20px"},
                                ),
                                html.Div(
                                    id="value-content",
                                    style={"marginTop": "20px"},
                                ),
                            ],
                            style={
                                "flex": "1",
                                "padding": "20px",
                                "overflowY": "auto",
                                "backgroundColor": "#f9f9f9",
                            },
                        ),
                    ],
                ),
            ]
        )
    ],
    fluid=True,
)

# 콜백: 마커 클릭 상태 업데이트
@app.callback(
    Output("marker-clicked", "data"),
    Input("map", "srcDoc"),
)
def update_marker_status(src_doc):
    return True

# 콜백: 버튼 표시/숨김 상태
@app.callback(
    Output("value-button-container", "children"),
    Input("marker-clicked", "data"),
)
def toggle_value_button(marker_clicked):
    # 버튼은 항상 생성, 클릭 여부는 내부 로직으로 처리
    return dbc.Button(
        "가성비",
        id="value-btn",
        color="primary",
        style={"width": "100%"},
    )

# 콜백: 가성비 리뷰 표시
@app.callback(
    Output("value-content", "children"),
    Input("value-btn", "n_clicks"),
    prevent_initial_call=True,  # 초기 콜백 실행 방지
)
def show_value_content(n_clicks):
    if n_clicks:
        filtered_data = data[data['Review'].str.contains(input(), na=False)]  # 'Review' 열 이름 사용
        return html.Ul([html.Li(review) for review in filtered_data['Review']])
    return ""

# 앱 실행
if __name__ == "__main__":
    app.run_server(debug=True)


