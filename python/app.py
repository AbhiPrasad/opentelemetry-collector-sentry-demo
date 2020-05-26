import flask
import requests
import os

import opentelemetry.ext.http_requests
from opentelemetry import trace

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.ext.otcollector.trace_exporter import CollectorSpanExporter

span_exporter = CollectorSpanExporter(
    service_name="basic-service", endpoint="localhost:55678"
)

tracer_provider = TracerProvider()
trace.set_tracer_provider(tracer_provider)
span_processor = BatchExportSpanProcessor(span_exporter)
tracer_provider.add_span_processor(span_processor)

app = flask.Flask(__name__)

@app.route("/")
def hello():
    tracer = trace.get_tracer_provider().get_tracer(__name__)
    with tracer.start_as_current_span('foo'):
        with tracer.start_as_current_span('bar'):
            with tracer.start_as_current_span('baz'):
                requests.get("http://www.example.com")
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)
