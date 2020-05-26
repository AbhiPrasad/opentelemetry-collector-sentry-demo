# SENTRY_KEY=d9e46d2369654b66a53a211060be8aa7

# curl -v -XPOST https://o19635.ingest.sentry.io/api/5248135/store/ \
#  -H 'Content-Type: application/json' \
#  -H "X-Sentry-Auth: Sentry sentry_version=7,sentry_timestamp=$(date +"%s"),sentry_client=sentry-curl/1.0,sentry_key=${SENTRY_KEY}" \
#  -d "$(cat ./ex.json)"
#  #

SENTRY_KEY=48b95f02bef84e17abde966511294457
SENTRY_API_URL=http://dev.getsentry.net:8000/api/8/store/

curl -v -XPOST ${SENTRY_API_URL} \
 -H 'Content-Type: application/json' \
 -H "X-Sentry-Auth: Sentry sentry_version=7,sentry_timestamp=$(date +"%s"),sentry_client=sentry-curl/1.0,sentry_key=${SENTRY_KEY}" \
 -d "$(cat ./small.json)"
