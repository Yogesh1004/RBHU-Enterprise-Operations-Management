import os
import logging
from flask import Flask, jsonify
from flask_cors import CORS
from routes.analytics_routes import analytics_bp

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("rbhu_analytics")

def create_app() -> Flask:
    app = Flask(__name__)

    # Configure CORS for enterprise frontend & backend communication
    allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
    CORS(app, resources={r"/*": {"origins": allowed_origins}}, supports_credentials=True)

    # Register blueprints
    app.register_blueprint(analytics_bp)

    @app.route("/", methods=["GET"])
    def root():
        return jsonify({
            "service": "RBHU Enterprise Sales Analytics Microservice",
            "status": "online",
            "endpoints": {
                "health": "/health",
                "sample_csv": "/sample-csv",
                "analyze": "POST /analyze (multipart/form-data with 'file')"
            }
        })

    @app.errorhandler(404)
    def handle_404(e):
        return jsonify({"success": False, "error": "Endpoint not found"}), 404

    @app.errorhandler(413)
    def handle_413(e):
        return jsonify({"success": False, "error": "Uploaded file exceeds maximum size limit (10MB)"}), 413

    @app.errorhandler(500)
    def handle_500(e):
        return jsonify({"success": False, "error": "Internal analytics server error"}), 500

    # Max upload size: 10MB
    app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("ANALYTICS_PORT", 5001))
    host = os.getenv("ANALYTICS_HOST", "0.0.0.0")
    logger.info(f"Starting RBHU Analytics Microservice on http://{host}:{port}")
    app.run(host=host, port=port, debug=False)
