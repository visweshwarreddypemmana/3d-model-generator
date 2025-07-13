from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    return jsonify({
        "status": "Running",
        "model": "Shap-E (Text & Image to 3D)"
    })

@app.route('/generate3d')
def generate3d():
    prompt = request.args.get('prompt')
    source = request.args.get('source', 'text')  # text or image
    
    if source == 'text':
        asset = "https://raw.githubusercontent.com/visweshwarreddypemmana/3d-model-generator/main/outputs/Chair.ply"
        preview = "https://raw.githubusercontent.com/visweshwarreddypemmana/3d-model-generator/blob/main/outputs/Chair.gif"
    else:
        asset = "https://raw.githubusercontent.com/visweshwarreddypemmana/3d-model-generator/blob/main/outputs/apple.obj"
        preview = "https://raw.githubusercontent.com/visweshwarreddypemmana/3d-model-generator/blob/main/outputs/apple.gif"

    return jsonify({
        "prompt": prompt,
        "source": source,
        "asset_url": asset,
        "preview_image": preview
    })

if __name__ == '__main__':
    app.run(debug=True)
