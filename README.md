# Sentry-demos/open-telemetry-collector

# WIP!

> Note: This is currently a WIP demo. As such, the structure and features of this demo will probably change

## Summary:
Shows how to use the Open Telemetry Sentry exporter (WIP) to send Open Telemetry traces to Sentry through the [Open Telemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)

- Leverages a docker based setup that runs the Open Telemetry Collector and Flask application
- Example Flask application generates Open Telemetry traces and sends those to the Open Telemetry collector
- Traces are then exported to Sentry through an custom Open Telemetry exporter (not yet built)
- Collects and displays traces in an Sentry instance

## To Run

Make sure you have docker installed.

```
docker-compose up
```



