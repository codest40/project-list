import time
import requests
import yaml
from prometheus_client import start_http_server, Summary, Counter, Gauge

# Metrics
REQUEST_LATENCY = Summary('api_response_latency_seconds', 'Response time in seconds', ['api_name'])
REQUEST_FAILURES = Counter('api_request_failures_total', 'Total request failures', ['api_name'])
UP_STATUS = Gauge('api_up', 'API up status (1=up, 0=down)', ['api_name'])

# Load config
def load_targets(path='config.yaml'):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    return data.get('targets', [])

# Check API
def check_api(api):
    name = api['name']
    url = api['url']
    method = api.get('method', 'GET').upper()

    try:
        with REQUEST_LATENCY.labels(api_name=name).time():
            response = requests.request(method, url, timeout=5)
        if response.status_code < 400:
            UP_STATUS.labels(api_name=name).set(1)
        else:
            REQUEST_FAILURES.labels(api_name=name).inc()
            UP_STATUS.labels(api_name=name).set(0)
    except Exception as e:
        REQUEST_FAILURES.labels(api_name=name).inc()
        UP_STATUS.labels(api_name=name).set(0)

# Main loop
if __name__ == "__main__":
    targets = load_targets()
    start_http_server(8000)  # Expose metrics on :8000/metrics
    print("✅ Uptime Tracker started on port 8000")

    while True:
        for target in targets:
            check_api(target)
        time.sleep(30)  # Check every 30 seconds
