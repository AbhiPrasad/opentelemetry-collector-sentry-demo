# Sentry-demos/open-telemetry-collector

# WIP!

> Note: This is currently a WIP demo. As such, the structure and features of this demo will probably change

## Summary:
Shows how to use the Open Telemetry Sentry exporter (WIP) to send Open Telemetry traces to Sentry through the [Open Telemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)

There are two examples in this demo. One is a script you can run against a running collector, while the other is a docker based setup that leverages [synthetic trace generation](https://github.com/Omnition/synthetic-load-generator) to create traces.

## Setup

Make sure you have docker installed.

Clone the `opentelemetry-collector-contrib`.

```bash
git clone git@github.com:getsentry/opentelemetry-collector-contrib.git
```

Run `make docker-otelcontribcol` to build the docker image.

## Simple Example



## To Run

Make sure you have docker installed.

```
docker-compose up
```



