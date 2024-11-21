# import dash
# from dash import html, Output, Input, dcc
# import dash_bootstrap_components as dbc
# import pandas as pd

# # CSV 파일 로드
# csv_path = 'C:/Fintech_service/10Final_PJT/뱅뱅막국수_combined_reviews.csv'
# data = pd.read_csv(csv_path)

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
#                         "height": "100vh",
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
#                                             strokeWeight: 2,
#                                             strokeColor: '#ff0000',
#                                             strokeOpacity: 0.8,
#                                             strokeStyle: 'dashed',
#                                             fillColor: '#ffcccc',
#                                             fillOpacity: 0.5
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
#                             style={"flex": "2", "borderRight": "1px solid #ccc"},
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
#                                 # 검색 박스 추가
#                                 dcc.Input(
#                                     id="search-box",
#                                     type="text",
#                                     placeholder="리뷰를 살펴보기 위한 검색어를 입력하세요.",
#                                     style={
#                                         "width": "100%",
#                                         "marginTop": "20px",
#                                         "padding": "10px",
#                                         "borderRadius": "5px",
#                                         "border": "1px solid #ddd",
#                                     },
#                                 ),
#                                 # 검색 결과 표시 영역
#                                 html.Div(
#                                     id="value-content",
#                                     style={"marginTop": "20px"},
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

# # 콜백: 검색 결과 표시
# @app.callback(
#     Output("value-content", "children"),
#     Input("search-box", "value"),
# )
# def search_reviews(search_term):
#     if search_term:
#         filtered_data = data[data['Review'].str.contains(search_term, na=False, case=False)]  # 대소문자 구분 없음
#         if not filtered_data.empty:
#             return html.Ul([html.Li(review) for review in filtered_data['Review']])
#         else:
#             return "검색 결과가 없습니다."
#     return ""

# # 앱 실행
# if __name__ == "__main__":
#     app.run_server(debug=True)



----------------------11.20



# import dash
# from dash import html, Output, Input, dcc
# import dash_bootstrap_components as dbc
# import pandas as pd

# # CSV 파일 로드
# google_data = pd.read_csv('bangbang_makguksu_reviews_google.csv')
# kakao_data = pd.read_csv('bangbang_makguksu_reviews_kakao.csv')
# naver_data = pd.read_csv('bangbang_makguksu_reviews_naver.csv')

# # Dash 앱 초기화
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# # 앱 레이아웃
# app.layout = dbc.Container(
#     [
#         dbc.Row(
#             [
#                 # 체크박스
#                 dbc.Col(
#                     [
#                         dbc.Checklist(
#                             id="platform-checkbox",
#                             options=[
#                                 {"label": "Naver", "value": "naver"},
#                                 {"label": "Google", "value": "google"},
#                                 {"label": "Kakao", "value": "kakao"},
#                             ],
#                             value=[],  # 초기 선택 없음
#                             inline=True,
#                         ),
#                         dcc.Input(
#                             id="search-box",
#                             type="text",
#                             placeholder="리뷰를 검색하세요.",
#                             style={
#                                 "width": "100%",
#                                 "marginTop": "20px",
#                                 "padding": "10px",
#                                 "borderRadius": "5px",
#                                 "border": "1px solid #ddd",
#                             },
#                         ),
#                         html.Div(id="review-content", style={"marginTop": "20px"}),
#                     ],
#                     width=4,
#                 ),
#                 # 지도 및 정보 패널 (기존 코드 유지)
#                 dbc.Col(
#                     [
#                         html.Iframe(
#                             id="map",
#                             srcDoc=f"""
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

#                                         var marker = new kakao.maps.Marker({{
#                                             position: new kakao.maps.LatLng(37.4896557, 127.0328555),
#                                             map: map
#                                         }});

#                                         kakao.maps.event.addListener(marker, 'click', function() {{
#                                             var infoPanel = window.parent.document.getElementById('info-panel-content');
#                                             infoPanel.innerHTML = `
#                                                 <div>
#                                                     <h4>뱅뱅막국수 역삼본점</h4>
#                                                     <p>서울 강남구 도곡로 112</p>
#                                                 </div>
#                                             `;
#                                         }});
#                                     </script>
#                                 </body>
#                                 </html>
#                             """,
#                             style={"width": "100%", "height": "600px", "border": "none"},
#                         )
#                     ],
#                     width=8,
#                 ),
#             ]
#         )
#     ],
#     fluid=True,
# )

# # 콜백: 체크박스 선택 및 검색 박스 동작
# @app.callback(
#     Output("review-content", "children"),
#     [Input("platform-checkbox", "value"), Input("search-box", "value")],
# )
# def update_reviews(selected_platforms, search_term):
#     if not selected_platforms:
#         return "리뷰를 보려면 플랫폼을 선택하세요."

#     combined_reviews = pd.DataFrame()
#     if "naver" in selected_platforms:
#         combined_reviews = pd.concat([combined_reviews, naver_data])
#     if "google" in selected_platforms:
#         combined_reviews = pd.concat([combined_reviews, google_data])
#     if "kakao" in selected_platforms:
#         combined_reviews = pd.concat([combined_reviews, kakao_data])

#     if search_term:
#         filtered_reviews = combined_reviews[
#             combined_reviews["Review"].str.contains(search_term, na=False, case=False)
#         ]
#     else:
#         filtered_reviews = combined_reviews

#     if not filtered_reviews.empty:
#         return html.Ul([html.Li(review) for review in filtered_reviews["Review"]])
#     else:
#         return "검색 결과가 없습니다."

# # 앱 실행
# if __name__ == "__main__":
#     app.run_server(debug=True)


# ----------------3사선택



# import dash
# from dash import html, Output, Input, dcc
# import dash_bootstrap_components as dbc
# import pandas as pd

# # CSV 파일 로드
# google_data = pd.read_csv('bangbang_makguksu_reviews_google.csv')
# kakao_data = pd.read_csv('bangbang_makguksu_reviews_kakao.csv')
# naver_data = pd.read_csv('bangbang_makguksu_reviews_naver.csv')

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
#                         "height": "100vh",
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

#                                         var marker = new kakao.maps.Marker({{
#                                             position: new kakao.maps.LatLng(37.4896557, 127.0328555),
#                                             map: map
#                                         }});

#                                         kakao.maps.event.addListener(marker, 'click', function() {{
#                                             var infoPanel = window.parent.document.getElementById('info-panel-content');
#                                             infoPanel.innerHTML = `
#                                                 <div>
#                                                     <h4>뱅뱅막국수 역삼본점</h4>
#                                                     <p>서울 강남구 도곡로 112</p>
#                                                 </div>
#                                             `;
#                                         }});
#                                     </script>
#                                 </body>
#                                 </html>
#                                 """,
#                                 style={"width": "100%", "height": "100%", "border": "none"},
#                             ),
#                             style={"flex": "2", "borderRight": "1px solid #ccc"},
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

#                                 # 새로운 체크박스 및 리뷰 영역
#                                 html.Div(
#                                     [
#                                         dbc.Checklist(
#                                             id="platform-checkbox",
#                                             options=[
#                                                 {"label": "Naver", "value": "naver"},
#                                                 {"label": "Google", "value": "google"},
#                                                 {"label": "Kakao", "value": "kakao"},
#                                             ],
#                                             value=[],  # 초기 선택 없음
#                                             inline=True,
#                                         ),
#                                         dcc.Input(
#                                             id="review-search-box",
#                                             type="text",
#                                             placeholder="리뷰를 검색하세요.",
#                                             style={
#                                                 "width": "100%",
#                                                 "marginTop": "20px",
#                                                 "padding": "10px",
#                                                 "borderRadius": "5px",
#                                                 "border": "1px solid #ddd",
#                                             },
#                                         ),
#                                         html.Div(
#                                             id="review-content",
#                                             style={"marginTop": "20px"},
#                                         ),
#                                     ],
#                                     style={"marginTop": "40px"},
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

# # 기존 검색 박스 콜백
# @app.callback(
#     Output("value-content", "children"),
#     Input("search-box", "value"),
# )
# def search_reviews(search_term):
#     if search_term:
#         filtered_data = google_data[google_data['Review'].str.contains(search_term, na=False, case=False)]
#         if not filtered_data.empty:
#             return html.Ul([html.Li(review) for review in filtered_data['Review']])
#         else:
#             return "검색 결과가 없습니다."
#     return ""

# # 새로운 체크박스 및 검색 콜백
# @app.callback(
#     Output("review-content", "children"),
#     [Input("platform-checkbox", "value"), Input("review-search-box", "value")],
# )
# def update_reviews(selected_platforms, search_term):
#     if not selected_platforms:
#         return "리뷰를 보려면 플랫폼을 선택하세요."

#     combined_reviews = pd.DataFrame()
#     if "naver" in selected_platforms:
#         combined_reviews = pd.concat([combined_reviews, naver_data])
#     if "google" in selected_platforms:
#         combined_reviews = pd.concat([combined_reviews, google_data])
#     if "kakao" in selected_platforms:
#         combined_reviews = pd.concat([combined_reviews, kakao_data])

#     if search_term:
#         filtered_reviews = combined_reviews[
#             combined_reviews["Review"].str.contains(search_term, na=False, case=False)
#         ]
#     else:
#         filtered_reviews = combined_reviews

#     if not filtered_reviews.empty:
#         return html.Ul([html.Li(review) for review in filtered_reviews["Review"]])
#     else:
#         return "검색 결과가 없습니다."

# # 앱 실행
# if __name__ == "__main__":
#     app.run_server(debug=True)


-------------11.20

import dash
from dash import html, Output, Input, dcc
import dash_bootstrap_components as dbc
import pandas as pd

# CSV 파일 로드
google_data = pd.read_csv('bangbang_makguksu_reviews_google.csv')
kakao_data = pd.read_csv('bangbang_makguksu_reviews_kakao.csv')
naver_data = pd.read_csv('bangbang_makguksu_reviews_naver.csv')

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
                        "height": "100vh",
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
                                            strokeWeight: 2,
                                            strokeColor: '#ff0000',
                                            strokeOpacity: 0.8,
                                            strokeStyle: 'dashed',
                                            fillColor: '#ffcccc',
                                            fillOpacity: 0.5
                                        }});
                                        circle.setMap(map);

                                        // 마커 설정
                                        var marker = new kakao.maps.Marker({{
                                            position: centerPosition,
                                            map: map
                                        }});

                                        // 마커 클릭 이벤트
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
                            style={"flex": "2", "borderRight": "1px solid #ccc"},
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

                                # 새로운 체크박스 및 검색 기능
                                html.Div(
                                    [
                                        dbc.Checklist(
                                            id="platform-checkbox",
                                            options=[
                                                {"label": "Naver", "value": "naver"},
                                                {"label": "Google", "value": "google"},
                                                {"label": "Kakao", "value": "kakao"},
                                            ],
                                            value=[],  # 초기 선택 없음
                                            inline=True,
                                        ),
                                        dcc.Input(
                                            id="review-search-box",
                                            type="text",
                                            placeholder="리뷰를 검색하세요.",
                                            style={
                                                "width": "100%",
                                                "marginTop": "20px",
                                                "padding": "10px",
                                                "borderRadius": "5px",
                                                "border": "1px solid #ddd",
                                            },
                                        ),
                                        html.Div(
                                            id="review-content",
                                            style={"marginTop": "20px"},
                                        ),
                                    ],
                                    style={"marginTop": "40px"},
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

# 기존 검색 박스 콜백
@app.callback(
    Output("value-content", "children"),
    Input("search-box", "value"),
)
def search_reviews(search_term):
    if search_term:
        filtered_data = google_data[google_data['Review'].str.contains(search_term, na=False, case=False)]
        if not filtered_data.empty:
            return html.Ul([html.Li(review) for review in filtered_data['Review']])
        else:
            return "검색 결과가 없습니다."
    return ""

# 새로운 체크박스 및 검색 콜백
@app.callback(
    Output("review-content", "children"),
    [Input("platform-checkbox", "value"), Input("review-search-box", "value")],
)
def update_reviews(selected_platforms, search_term):
    if not selected_platforms:
        return "리뷰를 보려면 플랫폼을 선택하세요."

    combined_reviews = pd.DataFrame()
    if "naver" in selected_platforms:
        combined_reviews = pd.concat([combined_reviews, naver_data])
    if "google" in selected_platforms:
        combined_reviews = pd.concat([combined_reviews, google_data])
    if "kakao" in selected_platforms:
        combined_reviews = pd.concat([combined_reviews, kakao_data])

    if search_term:
        filtered_reviews = combined_reviews[
            combined_reviews["Review"].str.contains(search_term, na=False, case=False)
        ]
    else:
        filtered_reviews = combined_reviews

    if not filtered_reviews.empty:
        return html.Ul([html.Li(review) for review in filtered_reviews["Review"]])
    else:
        return "검색 결과가 없습니다."

# 앱 실행
if __name__ == "__main__":
    app.run_server(debug=True)
