import os
import time

from opentelemetry import trace as otel_trace
from opentelemetry.ext.otcollector.trace_exporter import CollectorSpanExporter as otel_CollectorSpanExporter
from opentelemetry.sdk.trace import TracerProvider as otel_TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor as otel_BatchExportSpanProcessor

otel_exporter = otel_CollectorSpanExporter(
    service_name="basic-service", endpoint="localhost:55678")
otel_trace.set_tracer_provider(otel_TracerProvider())
otel_tracer = otel_trace.get_tracer(__name__)
otel_span_processor = otel_BatchExportSpanProcessor(otel_exporter)
otel_trace.get_tracer_provider().add_span_processor(otel_span_processor)

with otel_tracer.start_as_current_span("another-sample-trace"):
    with otel_tracer.start_as_current_span("bar"):
        time.sleep(2.4)
        with otel_tracer.start_as_current_span("baz"):
            time.sleep(0.5)
        with otel_tracer.start_as_current_span("kaps"):
            time.sleep(1)
