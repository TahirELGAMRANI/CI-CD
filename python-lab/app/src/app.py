from flask import Flask, jsonify
import os
import sys

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 5000))

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': __import__('datetime').datetime.now().isoformat()
    }), 200

@app.route('/', methods=['GET'])
def root():
    """Root endpoint"""
    return jsonify({
        'message': 'Welcome to CI/CD Python Application',
        'version': '1.0.0',
        'environment': os.environ.get('FLASK_ENV', 'development')
    }), 200

@app.route('/api/info', methods=['GET'])
def info():
    """API info endpoint"""
    return jsonify({
        'app': 'CI/CD Python Lab',
        'language': 'Python',
        'framework': 'Flask',
        'pythonVersion': sys.version.split()[0]
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)

