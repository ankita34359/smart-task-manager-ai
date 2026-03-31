import os
import logging
from flask import Flask, jsonify
from flask_cors import CORS

def create_app(config_name='development'):
    app = Flask(__name__)
    CORS(app)

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f'sqlite:///{os.path.join(basedir, "app.db")}')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from models import db
    import models.task  # Import models before create_all
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from routes.task_routes import task_bp
    app.register_blueprint(task_bp, url_prefix='/api/tasks')

    @app.route('/health')
    def health_check():
        return jsonify({"status": "healthy"}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        from models import db
        db.create_all()
    app.run(debug=True, port=5000)
