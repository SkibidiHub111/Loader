from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def lua_script():
    lua_code = '''local Games = loadstring(game:HttpGet("https://raw.githubusercontent.com/shinichi-dz/phucshinsayhi/refs/heads/main/loader.lua"))()

for PlaceID, Execute in pairs(Games) do
    if PlaceID == game.PlaceId then
        loadstring(game:HttpGet(Execute))()
    end
end'''

    
    return Response(lua_code, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
