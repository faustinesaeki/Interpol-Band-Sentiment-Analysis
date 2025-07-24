import base64


def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

#конвертация пикчи в base64
bg_image = img_to_base64("assets/2.jpg")

colors = ["#240104ff",
          "#808080ff",
          "#83000Bff",
          "#090908ff",
          "#490208ff",
          "#575657ff"]
    

#это треш
markdown = f"""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Yanone+Kaffeesatz:wght@200..700&display=swap" rel="stylesheet">

    <style>
        .stApp {{
            background: url('data:image/png;base64,{bg_image}') !important;
            background-size: cover !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            color: white !important;
            font-family: 'Yanone Kaffeesatz', sans-serif !important;
        }}

        * {{
            font-family: 'Yanone Kaffeesatz', sans-serif !important;
        }}

        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Yanone Kaffeesatz', sans-serif !important;
            color: white !important;
            text-align: center !important;
            text-shadow: 2px 2px 5px #575657ff;
        }}

        h1{{
            text-decoration: underline;
        }}

        .stImage caption {{
            font-family: 'Yanone Kaffeesatz', sans-serif !important;
            color: white !important;
            text-align: center !important;
            font-size: 1.2rem !important;
        }}

        header[data-testid="stHeader"] {{
            background: black !important;
            box-shadow: 0 0 8px 0 #090908ff !important;
            height: 75px !important;
        }}

        div[data-testid="stFullScreenFrame"] {{
            max-width: 95% !important;
            margin: 0 auto !important;
            display: flex !important;
            justify-content: center !important;
        }}

        div[data-testid="stHorizontalBlock"] {{
            justify-content: center !important;
        }}

        div[data-testid="stColumn"] {{
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
            padding: 10px !important;
            margin: 0 auto !important;
        }}

        div[data-testid="stImage"] {{
            width: 100% !important;
            max-width: 400px !important;
            margin: 0 auto !important;
        }}

        div[data-testid="stImage"] img {{
            width: 100% !important;
            height: auto !important;
            border-radius: 15px !important;
            box-shadow: 0 4px 8px black !important;
            transition: transform 0.3s ease !important;
        }}

        div[data-testid="stImage"] img:hover {{
            transform: scale(1.05) !important;
        }}

        div[data-testid="stPlotlyChart"] {{
            border: 2px solid #575657ff !important;
            border-radius: 15px !important;
            box-shadow: 0 4px 8px black !important;
            background: black !important;
            margin: 20px auto !important;
            padding: 15px !important;
        }}

        .st-bb, .st-at, .st-ae, .st-af, .st-ag, .stSelectbox, .stSlider {{
            font-family: 'Yanone Kaffeesatz', sans-serif !important;
        }}
        div[class="stElementToolbar st-emotion-cache-1iuhdj4 et0utro0"]{{
            display: none;
        }}

        div[data-testid="stDataFrameResizable"]{{
            box-shadow: 0 4px 8px black !important;
        }}

    </style>
        """    