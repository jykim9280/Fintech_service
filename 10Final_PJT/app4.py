# import dash
# from dash import html, Input, Output, State, dcc
# import dash_bootstrap_components as dbc

# # Dash 앱 초기화
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# # 앱 레이아웃
# app.layout = html.Div(
#     style={
#         "backgroundColor": "#f8f9fa",  # 앱 배경색
#         "width": "100%",
#         "height": "100vh",
#         "fontFamily": "Arial, sans-serif",
#         "display": "flex",
#         "flexDirection": "column",
#     },
#     children=[
#         # 상단 네비게이션 바
#         html.Div(
#             style={
#                 "display": "flex",
#                 "justifyContent": "space-between",
#                 "alignItems": "center",
#                 "backgroundColor": "#ffffff",
#                 "padding": "10px 15px",
#                 "borderBottom": "1px solid #ddd",
#             },
#             children=[
#                 html.H1(
#                     "ZZIN VIEW",
#                     style={
#                         "fontSize": "20px",
#                         "color": "#333",
#                         "margin": 0,
#                     },
#                 ),
#                 html.Div(
#                     style={"display": "flex", "alignItems": "center"},
#                     children=[
#                         html.Div(
#                             style={
#                                 "width": "8px",
#                                 "height": "8px",
#                                 "borderRadius": "50%",
#                                 "backgroundColor": "#ff5252",
#                                 "marginRight": "8px",
#                             }
#                         ),
#                         html.Span("9:41", style={"fontSize": "14px", "color": "#777"}),
#                     ],
#                 ),
#             ],
#         ),
#         # 검색 및 반경 설정 섹션
#         html.Div(
#             style={
#                 "padding": "15px",
#                 "backgroundColor": "#ffffff",
#                 "borderBottom": "1px solid #ddd",
#             },
#             children=[
#                 dcc.Input(
#                     id="address-input",
#                     type="text",
#                     placeholder="주소를 입력하세요.",
#                     style={
#                         "width": "100%",
#                         "padding": "10px",
#                         "border": "1px solid #ddd",
#                         "borderRadius": "5px",
#                         "marginBottom": "10px",
#                     },
#                 ),
#                 html.Div(
#                     style={"display": "flex", "justifyContent": "space-between"},
#                     children=[
#                         dcc.Dropdown(
#                             id="radius-dropdown",
#                             options=[
#                                 {"label": "100m", "value": 100},
#                                 {"label": "200m", "value": 200},
#                                 {"label": "300m", "value": 300},
#                                 {"label": "400m", "value": 400},
#                                 {"label": "500m", "value": 500},
#                             ],
#                             placeholder="반경 설정",
#                             style={"width": "48%", "borderRadius": "5px"},
#                         ),
#                         html.Button(
#                             "반경 표시",
#                             id="show-radius-button",
#                             n_clicks=0,
#                             style={
#                                 "width": "48%",
#                                 "padding": "10px",
#                                 "backgroundColor": "#007bff",
#                                 "color": "#fff",
#                                 "border": "none",
#                                 "borderRadius": "5px",
#                                 "cursor": "pointer",
#                             },
#                         ),
#                     ],
#                 ),
#             ],
#         ),
#         # 지도 영역
#         html.Div(
#             style={
#                 "flex": "1",
#                 "overflow": "hidden",
#                 "position": "relative",
#                 "backgroundColor": "#e9ecef",
#                 "width": "100%",
#             },
#             children=[
#                 html.Iframe(
#                     id="map",
#                     style={
#                         "width": "100%",
#                         "height": "100%",
#                         "border": "none",
#                         "position": "absolute",
#                         "top": 0,
#                         "left": 0,
#                     },
#                     srcDoc="""
#                     <!DOCTYPE html>
#                     <html>
#                     <head>
#                         <meta charset="utf-8">
#                         <title>Kakao Map</title>
#                         <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=809f4e8d66fb1289847f037850859b15"></script>
#                         <style>
#                             body, html { margin: 0; padding: 0; width: 100%; height: 100%; }
#                             #map { width: 100%; height: 100%; }
#                         </style>
#                     </head>
#                     <body>
#                         <div id="map"></div>
#                         <script>
#                             var mapContainer = document.getElementById('map'); 
#                             var mapOption = { 
#                                 center: new kakao.maps.LatLng(37.4896557, 127.0328555), 
#                                 level: 4 
#                             };
#                             var map = new kakao.maps.Map(mapContainer, mapOption);
#                         </script>
#                     </body>
#                     </html>
#                     """,
#                 ),
#             ],
#         ),
#         # 하단 내비게이션 바
#         html.Div(
#             style={
#                 "position": "absolute",
#                 "bottom": 0,
#                 "width": "100%",
#                 "backgroundColor": "#ffffff",
#                 "borderTop": "1px solid #ddd",
#                 "display": "flex",
#                 "justifyContent": "space-around",
#                 "padding": "10px 0",
#             },
#             children=[
#                 html.Div(
#                     style={"textAlign": "center"},
#                     children=[
#                         html.Span("🏠", style={"fontSize": "20px"}),
#                         html.Div("Home", style={"fontSize": "12px", "color": "#555"}),
#                     ],
#                 ),
#                 html.Div(
#                     style={"textAlign": "center"},
#                     children=[
#                         html.Span("📍", style={"fontSize": "20px"}),
#                         html.Div("Map", style={"fontSize": "12px", "color": "#555"}),
#                     ],
#                 ),
#                 html.Div(
#                     style={"textAlign": "center"},
#                     children=[
#                         html.Span("🔍", style={"fontSize": "20px"}),
#                         html.Div("Search", style={"fontSize": "12px", "color": "#555"}),
#                     ],
#                 ),
#                 html.Div(
#                     style={"textAlign": "center"},
#                     children=[
#                         html.Span("⚙️", style={"fontSize": "20px"}),
#                         html.Div("Settings", style={"fontSize": "12px", "color": "#555"}),
#                     ],
#                 ),
#             ],
#         ),
#     ],
# )

# # 콜백: 반경 설정 버튼 클릭
# @app.callback(
#     Output("map", "srcDoc"),
#     [Input("show-radius-button", "n_clicks")],
#     [State("radius-dropdown", "value")],
# )
# def update_radius(n_clicks, radius):
#     if n_clicks > 0 and radius:
#         return f"""
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <meta charset="utf-8">
#             <title>Kakao Map</title>
#             <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=809f4e8d66fb1289847f037850859b15"></script>
#             <style>
#                 body, html {{ margin: 0; padding: 0; width: 100%; height: 100%; }}
#                 #map {{ width: 100%; height: 100%; }}
#             </style>
#         </head>
#         <body>
#             <div id="map"></div>
#             <script>
#                 var mapContainer = document.getElementById('map'); 
#                 var mapOption = {{
#                     center: new kakao.maps.LatLng(37.4896557, 127.0328555), 
#                     level: 4 
#                 }};
#                 var map = new kakao.maps.Map(mapContainer, mapOption);
#                 var circle = new kakao.maps.Circle({{
#                     center: new kakao.maps.LatLng(37.4896557, 127.0328555),
#                     radius: {radius},
#                     strokeWeight: 2,
#                     strokeColor: '#ff0000',
#                     strokeOpacity: 0.8,
#                     fillColor: '#ffcccc',
#                     fillOpacity: 0.5
#                 }});
#                 circle.setMap(map);
#             </script>
#         </body>
#         </html>
#         """
#     return dash.no_update


# # 앱 실행
# if __name__ == "__main__":
#     app.run_server(debug=True)
# =======================================================


import pymysql
import dash
from dash import html, Input, Output, State, dcc
import dash_bootstrap_components as dbc

# MySQL 연결 설정 및 데이터 가져오기
def fetch_stores():
    connection = pymysql.connect(
        host='127.0.0.1',  # MySQL 서버 주소
        port=3306,  # 포트
        user='root',  # MySQL 사용자 이름
        password='1234',  # MySQL 비밀번호
        database='project',  # 데이터베이스 이름
        charset='utf8mb4'
    )
    query = "SELECT store_name, address FROM stores;"
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
    connection.close()
    return results

# Dash 앱 초기화
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 앱 레이아웃
app.layout = html.Div(
    style={
        "backgroundColor": "#f8f9fa",
        "width": "100%",
        "height": "100vh",
        "fontFamily": "Arial, sans-serif",
        "display": "flex",
        "flexDirection": "column",
    },
    children=[
        html.Div(
            style={
                "padding": "15px",
                "backgroundColor": "#ffffff",
                "borderBottom": "1px solid #ddd",
            },
            children=[
                html.H1(
                    "ZZIN VIEW",
                    style={
                        "fontSize": "20px",
                        "color": "#333",
                        "margin": 0,
                    },
                ),
            ],
        ),
        html.Div(
            style={
                "flex": "1",
                "overflow": "hidden",
                "position": "relative",
                "backgroundColor": "#e9ecef",
                "width": "100%",
            },
            children=[
                html.Iframe(
                    id="map",
                    style={
                        "width": "100%",
                        "height": "100%",
                        "border": "none",
                        "position": "absolute",
                        "top": 0,
                        "left": 0,
                    },
                ),
            ],
        ),
    ],
)

# 콜백: 지도 업데이트
@app.callback(
    Output("map", "srcDoc"),
    [Input("map", "id")]  # 임의 Input으로 콜백 트리거
)
def update_map(_):
    # 데이터베이스에서 가게 정보 가져오기
    stores = fetch_stores()

    # JavaScript로 마커 생성 코드 작성
    markers_js = "\n".join([
        f"""
        var geocoder = new kakao.maps.services.Geocoder();
        geocoder.addressSearch('{store[1]}', function(result, status) {{
            if (status === kakao.maps.services.Status.OK) {{
                var marker = new kakao.maps.Marker({{
                    position: new kakao.maps.LatLng(result[0].y, result[0].x),
                    map: map,
                    title: '{store[0]}'
                }});
            }}
        }});
        """ for store in stores
    ])

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Kakao Map</title>
        <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=809f4e8d66fb1289847f037850859b15&libraries=services"></script>
        <style>
            body, html {{ margin: 0; padding: 0; width: 100%; height: 100%; }}
            #map {{ width: 100%; height: 100%; }}
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            var mapContainer = document.getElementById('map'); 
            var mapOption = {{
                center: new kakao.maps.LatLng(37.4896557, 127.0328555),
                level: 4
            }};
            var map = new kakao.maps.Map(mapContainer, mapOption);
            
            // 마커 추가
            {markers_js}
        </script>
    </body>
    </html>
    """

# 앱 실행
if __name__ == "__main__":
    app.run_server(debug=True)

