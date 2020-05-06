# Based on https://github.com/open-telemetry/opentelemetry-python/blob/master/docs/getting-started.rst
from opentelemetry.ext.flask import FlaskInstrumentor
FlaskInstrumentor().instrument()  # This needs to be executed before importing Flask

import flask
import requests
import os

import opentelemetry.ext.http_requests
from opentelemetry import trace

from opentelemetry.ext.flask import instrument_app
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.ext.otcollector.trace_exporter import CollectorSpanExporter

trace.set_tracer_provider(TracerProvider())

exporter = CollectorSpanExporter(
    service_name="basic-service", endpoint="localhost:55678"
)

span_processor = BatchExportSpanProcessor(exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

app = flask.Flask(__name__)
instrument_app(app)
opentelemetry.ext.http_requests.RequestsInstrumentor().instrument()

@app.route("/")
def hello():
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span('foo'):
        with tracer.start_as_current_span('bar'):
            with tracer.start_as_current_span('baz'):
                requests.get("http://www.example.com")
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)
