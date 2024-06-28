from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/getDailyImage', methods=['GET'])
def getDailyImage():
    url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=es-AR'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        
        # Obtener el contenido de la respuesta como texto
        response_content = response.text
        
        # Devolver el contenido como JSON
        return jsonify({"image": response_content})
    
    except requests.exceptions.RequestException as e:
        # Manejar cualquier error de solicitud
        return jsonify({"error": str(e)})


@app.rout("/")
def root():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
