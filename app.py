from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def lua_script():
    url = "https://cdn.discordapp.com/attachments/1428012794678087950/1428998137539854336/6652138009334659.lua?ex=68f53279&is=68f3e0f9&hm=2dfdfbf80d8a3adf67bc303aadc6ff30ba53ef7880851d2f226d84f774e122e8&"
    response = requests.get(url)
    if response.status_code == 200:
        lua_code = response.text
    else:
        lua_code = "Error: Không thể tải file Lua từ URL"
    return Response(lua_code, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
