from flask import Flask
from prometheus_client import start_http_server, Counter, Histogram, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
from flask import Response
import time
 
app = Flask(__name__)
 
# Custom metrics
REQUEST_COUNT = Counter("request_count", "Total number of requests")
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency")
 
@app.route("/")
def home():
   REQUEST_COUNT.inc()
   with REQUEST_LATENCY.time():
       time.sleep(0.1)  # simulate processing
   return "Hello from Raman Micro!"
 
# Expose Prometheus metrics at /metrics
@app.route("/metrics")
def metrics():
   return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
 
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
