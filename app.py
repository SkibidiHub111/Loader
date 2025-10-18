from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def lua_script():
    lua_code = '''https://cdn.discordapp.com/attachments/1383960373643968613/1428981126776492122/Output.lua?ex=68f479e1&is=68f32861&hm=6c28684051966a7d8e6f2ff6165a67245b99fd1ffdb0696bc945c80640d0312c&'''
    return Response(lua_code, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
