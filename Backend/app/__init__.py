import os
from flask import Flask

def create_app():
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Frontend/templates'))
    static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Frontend/static'))

    app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
    app.config.from_object('app.config.Config')

    # Debugging: Print the absolute paths to the template and static folders
    print("Template folder absolute path:", template_dir)
    print("Static folder absolute path:", static_dir)

    # Register Blueprints or import routes
    with app.app_context():
        from . import routes

    return app
