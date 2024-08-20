# This files runs our flask application 

from app import create_app

#prebuilt models stored in a list
prebuilt_models = ["prebuilt-invoice", "prebuilt-receipts", "prebuilt-reports", "prebuilt-admissionforms"]

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

    