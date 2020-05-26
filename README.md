# Sentry-demos/open-telemetry-collector

# WIP!

> Note: This is currently a WIP demo. As such, the structure and features of this demo will probably change

## Summary:
Shows how to use the Open Telemetry Sentry exporter (WIP) to send Open Telemetry traces to Sentry through the [Open Telemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)

There are two examples in this demo. One is a script you can run against a running collector, while the other is a docker based setup that leverages [synthetic trace generation](https://github.com/Omnition/synthetic-load-generator) to create traces.

## Setup

Make sure you have docker and Python3 installed.

In another folder, clone the `opentelemetry-collector-contrib` repo.

```bash
git clone git@github.com:getsentry/opentelemetry-collector-contrib.git
```

Run `make docker-otelcontribcol` to build the docker image. It should be tagged as `otelcontribcol:latest`. If you have another image you prefer to use, change the image used in the `docker-compose`.

## Simple Example

Change directory to the simple example

```bash
cd simple_example
```

Setup and activate a Python3 environment.

```bash
python3 -m pip install virtualenv
python3 -m virtualenv .venv
source .venv/bin/activate
```

Install all required dependencies.

```bash
pip install -r requirements.txt
```

If needed, you can deactivate your virtualenv using:

```bash
deactivate
```

Add a DSN to your local config.

> simple_example/config.yaml
```yaml
...
exporters:
  logging: {}
  sentry:
    dsn: INSERT_DSN_HERE
...
```

Run the opentelemetry collector.

```bash
cd PATH_TO_CLONED/opentelemetry-collector-contrib
make otelcontribcol && GO111MODULE=on go run --race ./cmd/otelcontribcol/... --config "PATH_TO/opentelemetry-collector-demo/simple_example/config.yaml"  --metrics-addr "localhost:1337"
```

Run the demo script

```bash
cd PATH_TO_CLONED/opentelemetry-collector-demo/simple_example
python script.py
```

You should see a trace now appear in Sentry.

## Docker example

#### Note: this example generates fake traces using a synthetic load generator, so it is recommended that a local sentry install be used to prevent sentry quota issues. 

Enter the example folder.

```bash
cd docker_example
```

Add a DSN to the `otel-agent-config.yaml` and `otel-collector-config.yaml` configs

If you are using a local sentry install, make sure to use `host.docker.internal` so docker can resolve the hosts properly

```yaml
...
exporters:
  logging:
  sentry:
    dsn: INSERT_DSN_HERE
...
```

Run docker-compose

```bash
docker-compose up
```

You should see traces come into Sentry.
