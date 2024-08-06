# Intellicoders Project

Intellicoders is a Flask-based web application that integrates basic JavaScript functionality. The project is designed to handle file uploads, interact with the Azure OCR API, and display results directly on the web interface.

## Features
- **File Upload**: Drag-and-drop or click to upload files.
- **Azure OCR Integration**: Send uploaded files to Azure OCR API for text extraction.
- **JavaScript Functionality**: Basic JavaScript integrated and served via Flask.

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine using: git clone https://github.com/yourusername/intellicoders.git

### 2. Navigate to the Backend Folder
Change your directory to the Backend folder: cd intellicoders/Backend

### 3. Set Up a Virtual Environment
Set up a virtual environment in the `/Backend` folder: python -m venv venv


### 4. Activate the Virtual Environment
Activate the virtual environment:
- On macOS/Linux:
    ```
    source venv/bin/activate
    ```
- On Windows:
    ```
    .\venv\Scripts\activate
    ```

### 5. Install Dependencies
Install the required dependencies: pip install flask requests

### 6. Run the Flask App
Run the Flask application: python run.py


## Gitignore Files

The following files and directories should be included but have been left out: intellicoders/Backend/app/config.py

## Project Structure

The project structure should look like this:

Intellicoders/
├── Backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── config.py
│ │ └── routes.py
│ ├── instance/
│ │ ├── config.py
│ ├── requirements.txt
│ └── run.py
├── Frontend/
│ ├── assets/
│ │ ├── shapes at 24-07-17 20.29.26.png
│ │ └── top_left_logo_.png
│ ├── scripts/
│ │ └── script.js
│ ├── styling/
│ │ └── style.css
│ └── templates/
│ └── index.html
└── .gitignore


## How It Works

### 1. File Upload
The user can upload files via a drag-and-drop interface or by clicking a button. The uploaded files are sent to the Flask backend for processing.

### 2. Azure OCR API
The uploaded file is sent to the Azure OCR API for text extraction. The extracted text is then sent back to the frontend and displayed on the web interface.

### 3. JavaScript Integration
The project includes basic JavaScript functionality, such as handling file uploads and toggling dark mode, which is served via Flask.

---

This README should provide a comprehensive guide to setting up and understanding the Intellicoders project. If you have any questions or need further assistance, feel free to reach out!













