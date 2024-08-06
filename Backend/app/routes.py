from flask import current_app as app, render_template, request, jsonify
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential


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

    document_analysis_client = DocumentAnalysisClient(
        endpoint=app.config['AZURE_ENDPOINT'],
        credential=AzureKeyCredential(app.config['AZURE_KEY'])
    )

    poller = document_analysis_client.begin_analyze_document(
        "prebuilt-invoice", image_data
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