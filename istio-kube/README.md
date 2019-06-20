
## URLs

http://localhost:16686


![Simple Sidecar Proxy](img/sidecar-proxy-simple.svg)


Kubernetes UI:
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/aio/deploy/recommended/kubernetes-dashboard.yaml

kubectl proxy

Dashboard:
http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/

Get Token:
kubectl -n kube-system get secret


Get Token:
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | awk '/^deployment-controller-token-/{print $1}') | awk '$1=="token:"{print $2}'


Get Token:
kubectl -n kube-system describe secret kubernetes-dashboard-token-cwkp8

Get All Tokens:
kubectl -n kube-system describe secret