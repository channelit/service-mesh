
### Steps
``` shell
kubectl apply -f install/kubernetes/istio-demo.yaml
kubectl apply -f kube_all_svc.yml
kubectl apply -f kube_httpbin.yml
kubectl apply -f kube_ingress.yml
kubectl apply -f kube_rules_all.yml
```
><http://localhost/status>

![Simple Sidecar Proxy](img/sidecar-proxy-simple.svg)


### Kubernetes Dashboard
``` shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/aio/deploy/recommended/kubernetes-dashboard.yaml

kubectl proxy
```
><http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login>

#### Login:
``` shell
-- Get Tokan
kubectl -n kube-system get secret

kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | awk '/^deployment-controller-token-/{print $1}') | awk '$1=="token:"{print $2}'

-- Get Token:
kubectl -n kube-system describe secret kubernetes-dashboard-token-cwkp8

-- Get All Tokens:
kubectl -n kube-system describe secret

```

### Grafana
``` shell
kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=grafana -o jsonpath='{.items[0].metadata.name}') 3000:3000 &
```
><http://localhost:3000/>

### Kiali
``` shell
KIALI_USERNAME=$(read -p 'Kiali Username: ' uval && echo -n $uval | base64)
KIALI_PASSPHRASE=$(read -sp 'Kiali Passphrase: ' pval && echo -n $pval | base64)

cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: kiali
  namespace: $NAMESPACE
  labels:
    app: kiali
type: Opaque
data:
  username: $KIALI_USERNAME
  passphrase: $KIALI_PASSPHRASE
EOF

kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=kiali -o jsonpath='{.items[0].metadata.name}') 20001:20001 &
```
><http://localhost:20001/kiali/console>
