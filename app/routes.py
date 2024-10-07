from flask import Blueprint, jsonify, request
import requests

mirror_endpoint = Blueprint('mirror_endpoint', __name__)

API_URL = "https://api.bloxflip.com"

def mirror_bloxflip(endpoint):
    url = f"{API_URL}/{endpoint}"
    method = request.method.lower()

    method_map = {
        'get': requests.get,
        'post': requests.post,
        'put': requests.put,
        'delete': requests.delete
    }

    try:
        if method not in method_map:
            return jsonify({"error": "Unsupported HTTP method"}), 405

        headers = {**request.headers}
        headers['Content-Type'] = 'application/json'
        headers.pop('Host', None)

        kwargs = {'headers': headers}
        if method in ['get', 'delete']:
            kwargs['params'] = request.args
        else:
            kwargs['json'] = request.get_json(force=True, silent=True) or {}

        resp = method_map[method](url, **kwargs)
        return resp.content, resp.status_code, {'Content-Type': 'application/json'}
    except requests.exceptions.RequestException:
        return jsonify({"error": "Failed to connect to Bloxflip API"}), 503

@mirror_endpoint.route('/<path:endpoint>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def mirror_any_endpoint(endpoint):
    return mirror_bloxflip(endpoint)