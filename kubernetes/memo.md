## Cheat Sheet
* `kubectl apply -f xxx.yaml`
* `kubectl get all`
* `kubectl get svc/deploy/pod`
* `kubectl get svc/deploy/pod xxx -o yaml`
* `kubectl get svc/deploy/pod xxx --show-labels`
* `kubectl delete svc/deploy/pod xxx`
* `kubectl delete pod pod-59b5fdc6dc-ks7gk`
* `kubectl describe pod_name`
* `kubectl logs pod_name container_name`
* `kubectl logs -l key=value`
* `kubectl exec --stdin --tty pod_name -c container_name -- /bin/bash`
* `kubectl top pod pod_name --containers`
* `kubectl cp pod_name:var/log/1.log -c container_name 1.log`
* `kubectl get pods --sort-by='.status.containerStatuses[0].restartCount'`

## 用 Minikube 跑 Service type 為 NodePort 或 Loadbalancer 無 External-IP 問題
1. `minikube tunnel`

## 如何 Build image 讓 minikube 裡 cluster 也讀得到
1. `$(minikube docker-env)`
2. `docker build -t xxx-image .`
3. Set image to `containers.name=xxx-image`
4. `imagePullPolicy` to Never
5. [Reference](https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube)

## 怎知道 Service 的 domain name 是什麼
- Service 的 domain name 有一個格式(底下)
- `<service_name>.<namespace_name>.svc.cluster.local` 
- 例如有個 `namespace=default` , `service_name=nginx` , 那麼此 `Service` 的 domain name 為 `nginx.default.svc.cluster.local` , 其他 `Pod` 可以透過此 doamin 存取 `nginx` 相關服務
