import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    app.config.from_mapping(
        SECRET_KEY='rogeliosolorzanoescobar',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )
    
<<<<<<< HEAD
=======
    from . import db
    db.init_app(app)
    
>>>>>>> 08fa88b (jhgjhg)
    @app.route('/hola')
    def hola():
        return 'Hola mundirijillo'
    
    return app