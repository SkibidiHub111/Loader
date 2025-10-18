from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def lua_script():
    lua_code = '''
repeat wait() until game:IsLoaded() and game.Players.LocalPlayer
getgenv().Config = getgenv().Config or {}
local v_1 = loadstring(game:HttpGet("https://cdn.discordapp.com/attachments/.../code_chinh.lua"))()
v_1()
'''
    return Response(lua_code, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
