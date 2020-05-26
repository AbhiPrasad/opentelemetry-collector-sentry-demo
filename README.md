# Sentry-demos/open-telemetry-collector

# WIP!

> Note: This is currently a WIP demo. As such, the structure and features of this demo will probably change

## Summary:
Shows how to use the Open Telemetry Sentry exporter (WIP) to send Open Telemetry traces to Sentry through the [Open Telemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)

There are two examples in this demo. One is a script you can run against a running collector, while the other is a docker based setup that leverages [synthetic trace generation](https://github.com/Omnition/synthetic-load-generator) to create traces.

## Setup

Make sure you have docker installed.

In another folder, clone the `opentelemetry-collector-contrib` repo.

```bash
git clone git@github.com:getsentry/opentelemetry-collector-contrib.git
```

Run `make docker-otelcontribcol` to build the docker image. It should be tagged as `otelcontribcol:latest`. If you have another image you prefer to use, change the image used in the `docker-compose`.

## Simple Example

Change directory to the simple example



## To Run

Make sure you have docker installed.

```
docker-compose up
```



