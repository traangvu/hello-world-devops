from flask import Flask, Response, send_from_directory
import time
import os
import socket
from prometheus_client import generate_latest, Histogram, CONTENT_TYPE_LATEST, REGISTRY

app = Flask(__name__)

# Histogram to track latency for all HTTP requests
REQUEST_LATENCY = Histogram(
    'hello_world_request_latency_seconds',
    'Latency for serving hello world',
    buckets=(0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5)
)

# Decorator to measure latency
def track_latency(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        REQUEST_LATENCY.observe(duration)
        return result
    wrapper.__name__ = func.__name__  # Flask requires the function name
    return wrapper

@app.route('/')
@track_latency
def hello_world():
    # Simulate work
    time.sleep(0.01)
    return 'hello world\n'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

@app.route('/metrics')
def metrics():
    """Expose Prometheus metrics"""
    data = generate_latest(REGISTRY)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)

def pick_port():
    """Pick port from env, or try requested port, otherwise ask OS for a free port."""
    env_port = os.getenv("PORT")
    if env_port:
        try:
            return int(env_port)
        except ValueError:
            pass
    requested = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(('', requested))
        s.close()
        return requested
    except OSError:
        try:
            s = socket.socket()
            s.bind(('', 0))
            port = s.getsockname()[1]
            s.close()
            return port
        except Exception:
            return 0

if __name__ == '__main__':
    port = pick_port()
    print(f"Starting Flask on port {port}")
    app.run(host='0.0.0.0', port=port)
