from flask import current_app as app, render_template, request, jsonify
import requests


# Render App form index.html
@app.route('/')
def index():
    return render_template('index.html')

# App Drag and Drop File Backend 
@app.route('/upload', methods=['POST'])
def upload(): 
    if 'file' not in request.files: 
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    image_data = file.read() 
    headers = {
        'Ocp-Apim-Subscription-Key': app.config['AZURE_KEY'],
        'Content-Type': 'application/octet-stream'
    }

    response = requests.post(app.config['AZURE_ENDPOINT'], headers=headers, data=image_data)
    response.raise_for_status()

    analysis = response.json()

    return jsonify(analysis)


"""

App Routing means mapping the URLs to a specific function that will handle the logic for that URL. Modern web frameworks use more meaningful URLs to help users remember the URLs and make navigation simpler.
@app.route('/'): Defines the route for the home page.


render_template('index.html'): Renders the index.html template.


@app.route('/process', methods=['POST']): Defines the route for processing the form submission.


Handles file upload and sends it to the Azure OCR API.

"""