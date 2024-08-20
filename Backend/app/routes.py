from flask import current_app as app, render_template, request, jsonify, redirect, url_for
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from run import prebuilt_models
import sys


#current model
currentModel = "prebuilt-admissionforms"

# Render App form index.html
@app.route('/')
def index():
    global currentModel
    return render_template('index.html', prebuilt_models=prebuilt_models, currentModel=currentModel)

@app.route('/select_model', methods=['POST'])
def select_model():
    data = request.json
    selected_model = data.get('model')
    # Store the selected model or perform other logic
    global currentModel
    currentModel = selected_model
    return redirect(url_for('index'))

# App Drag and Drop File Backend 
@app.route('/upload', methods=['POST'])
def upload():
    global currentModel

    if 'file' not in request.files: 
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    image_data = file.read() 

    document_analysis_client = DocumentAnalysisClient(
        endpoint=app.config['AZURE_ENDPOINT'],
        credential=AzureKeyCredential(app.config['AZURE_KEY'])
    )

    #debugging
    print(f'in Upload using Model: {currentModel}')
    
    if not currentModel:
        return 'no model selected', 400
    
    #call azure API with the selected model
    poller = document_analysis_client.begin_analyze_document(
        model_id=currentModel, document=image_data
    )

    result = poller.result()

    # Process the result as needed
    print(jsonify(result.to_dict()))
    return jsonify(result.to_dict())

"""

App Routing means mapping the URLs to a specific function that will handle the logic for that URL. Modern web frameworks use more meaningful URLs to help users remember the URLs and make navigation simpler.
@app.route('/'): Defines the route for the home page.


render_template('index.html'): Renders the index.html template.


@app.route('/process', methods=['POST']): Defines the route for processing the form submission.


Handles file upload and sends it to the Azure OCR API.

"""