

# opentelemetry-collector-sentry-demo

Hola, ¿te interesa una mejor forma de integrar Sentry y OpenTelemetry? Por favor, consulta: https://github.com/getsentry/sentry/discussions/40712

## Resumen:

Muestra cómo utilizar el exportador de OpenTelemetry para Sentry (en desarrollo) para enviar trazas de OpenTelemetry a Sentry a través del [Open Telemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)

Hay dos ejemplos en esta demostración. Uno es un script que puedes ejecutar contra un colector en ejecución, mientras que el otro es una configuración basada en Docker que aprovecha la [generación de trazas sintéticas](https://github.com/Omnition/synthetic-load-generator) para crear trazas.

## Configuración

Asegúrate de tener Docker y Go instalados.

Clona este repositorio:

```
git clone git@github.com:AbhiPrasad/opentelemetry-collector-sentry-demo.git
```

En otra carpeta, clona el repositorio `opentelemetry-collector-contrib`.

```bash
git clone git@github.com:getsentry/opentelemetry-collector-contrib.git
```

## Ejemplo simple

Cambia al directorio del ejemplo simple

```bash
cd simple_example
```

Configura y activa un entorno de Python 3.

```bash
python3 -m pip install virtualenv
python3 -m virtualenv .venv
source .venv/bin/activate
```

Instala todas las dependencias requeridas.

```bash
pip install -r requirements.txt
```

Si es necesario, puedes desactivar tu virtualenv utilizando:

```bash
deactivate
```

Agrega un DSN a tu configuración local.

> simple_example/config.yaml

```yaml
---
exporters:
  logging: {}
  sentry:
    dsn: INSERT_DSN_HERE
```

Ejecuta el colector de OpenTelemetry.

```bash
cd path/to/cloned/opentelemetry-collector-contrib
make otelcontribcol && GO111MODULE=on go run --race ./cmd/otelcontribcol/... --config "PATH_TO/opentelemetry-collector-sentry-demo/simple_example/config.yaml"  --metrics-addr "localhost:1337"
```

Ejecuta el script de demostración

```bash
cd path/to/cloned/opentelemetry-collector-sentry-demo/simple_example
python script.py
```

Ahora deberías ver aparecer una traza en Sentry.

## Ejemplo con Docker

#### Nota: este ejemplo genera trazas falsas utilizando un generador de carga sintética, por lo que se recomienda utilizar una instalación local de Sentry para evitar problemas de cuota de Sentry.

Ingresa al proyecto clonado y genera la imagen de Docker. Debería estar etiquetada como `otelcontribcol:latest`. Si prefieres usar otra imagen, cambia la imagen utilizada en el `docker-compose`.

```bash
cd path/to/cloned/opentelemetry-collector-contrib
make docker-otelcontribcol
```

Ahora, navega a la carpeta `docker_example` desde la demostración.

```bash
cd path/to/cloned/opentelemetry-collector-sentry-demo/docker_example
```

Agrega el DSN de tu proyecto de Sentry a las configuraciones `otel-agent-config.yaml` y `otel-collector-config.yaml`

Si estás utilizando una instalación local de Sentry, asegúrate de usar `host.docker.internal` para que Docker pueda resolver los hosts correctamente

```yaml
---
exporters:
  logging:
  sentry:
    dsn: INSERT_DSN_HERE
```

Ejecuta docker-compose

```bash
docker-compose up
```

Deberías ver llegar trazas a Sentry.
