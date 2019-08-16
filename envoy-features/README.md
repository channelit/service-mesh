
# Envoy configuration with JWT authentication using Keycloak


## URLs

Services: http://localhost:8080
Jaeger: http://localhost:16686
Prometheus: http://localhost:9090
Graphana: http://localhost:3001
Keycloak: http://localhost:8080
Locsust: http://localhost:8089/

## Run Locust locally (won't work unless mapped localhost)

docker run --name=locust -v $(pwd)/locust-jwt.py:/locust.py -p 8421:8089 -e URL_HOST=localhost -e URL_PORT=8090 -e JWT_URL=http://localhost:8080 --network="host" cithub/locust locust -f /locust.py

![Simple Sidecar Proxy](img/sidecar-proxy-simple.svg)

## Steps:

1. docker-compose up
2. Create user in Keycloak
3. Validate user in Postman
4. Run locust for 200 users
5. Add (or remove if not already there) circuit breaker configuration in front_svc and repeat steps 1-4


### Get token
``` shell
curl --request POST \
  --url http://localhost:8080/auth/realms/envoy/protocol/openid-connect/token \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data 'username=user&password=user&grant_type=password&client_id=envoy'
  ```

### Get response using JWT token (insert token from above command)

``` shell
curl --request GET \
  --url http://localhost:8090/client \
  --header 'Postman-Token: <TOKEN>' \
  --header 'cache-control: no-cache'
```