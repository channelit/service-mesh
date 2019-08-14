
# Envoy configuration with JWT authentication using Keycloak


## URLs

Services: http://localhost:8080
Jaeger: http://localhost:16686
Prometheus: http://localhost:9090
Graphana: http://localhost:3001

## Run Locust locally (won't work unless mapped localhost)

docker run --name=locust -v $(pwd)/locust-jwt.py:/locust.py -p 8421:8089 -e URL_HOST=localhost -e URL_PORT=8090 -e JWT_URL=http://localhost:8080 cithub/locust locust -f /locust.py

![Simple Sidecar Proxy](img/sidecar-proxy-simple.svg)