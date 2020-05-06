# Based on https://github.com/open-telemetry/opentelemetry-python/blob/master/docs/getting-started.rst
from opentelemetry.ext.flask import FlaskInstrumentor
FlaskInstrumentor().instrument()  # This needs to be executed before importing Flask

import flask
import requests

import opentelemetry.ext.http_requests
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import SimpleExportSpanProcessor

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(ConsoleSpanExporter())
)

app = flask.Flask(__name__)
opentelemetry.ext.http_requests.enable(trace.get_tracer_provider())

@app.route("/")
def hello():
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("example-request"):
        requests.get("http://www.example.com")
    return "hello"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
