# Simple Flask website for Revelion 2025-2026
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'/>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'/>
  <title>Revelion 2025-2026</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      background: #f7c1d9;
      text-align: center;
    }
    .container { padding: 40px; }
    h1 {
      color: #ffffff;
      font-size: 36px;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .marijuana-gallery img {
      width: 250px;
      margin: 10px;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    #mainButton {
      background: #ffffff;
      color: #000000;
      padding: 20px 40px;
      font-size: 28px;
      border: none;
      border-radius: 16px;
      cursor: pointer;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
      transition: transform 0.2s;
    }
    #mainButton:active { transform: scale(0.96); }
    #message {
      margin-top: 30px;
      font-size: 24px;
      font-weight: bold;
      color: #ffffff;
    }
  </style>
</head>
<body>
  <div class='container'>
    <h1>Revelion 2025 - 2026</h1>

    <div class='marijuana-gallery'>
      <img src='https://upload.wikimedia.org/wikipedia/commons/5/5f/Cannabis_plant.jpg' />
      <img src='https://upload.wikimedia.org/wikipedia/commons/7/70/Cannabis_flowering.jpg' />
    </div>

    <button id='mainButton' onclick='showMessage()'>REVELION 2025-2026 TAP HERE</button>
    <div id='message'></div>
  </div>

  <script>
    function showMessage() {
      document.getElementById('message').textContent = 
        'SORRY GUYS BUT THIS NEW YEAR WE WILL NOT BE TOGETHER';
    }
  </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(debug=True)
