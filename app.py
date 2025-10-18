from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def lua_script():
    url = "https://cdn.discordapp.com/attachments/1428012794678087950/1428998120167178291/KTHCY.lua_2_1_1_2_3_2.txt?ex=68f53275&is=68f3e0f5&hm=affcec770fcd29495aa65b448d8486b616aa549a6265e4542dcb0016a11a39bd&"
    response = requests.get(url)
    if response.status_code == 200:
        lua_code = response.text
    else:
        lua_code = "Error: Không thể tải file Lua từ URL"
    return Response(lua_code, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
