# Setup a permissioned Ethereum blockchain on Kubernetes

1.  Generate Kubernetes manifest files
2.  Create secrets
3.  Apply manifest files
4.  Verify Ethereum network

## 1. Generate Kubernetes manifest files

```bash
source authority/.env.authority1
envsubst \$AUTHORITY_NAME,\$NFS_SERVER,\$NFS_PATH,\$NETWORK_ID,\$BOOT_NODE_ID,\$AUTHORITY_ADDRESS < authority/authority.template.yaml > authority1.yaml

source authority/.env.authority2
envsubst \$AUTHORITY_NAME,\$NFS_SERVER,\$NFS_PATH,\$NETWORK_ID,\$BOOT_NODE_ID,\$AUTHORITY_ADDRESS < authority/authority.template.yaml > authority2.yaml
```

## 2. Create secrets

```bash
kubectl create secret generic bootkey --from-file=boot.key
kubectl create secret generic genesis --from-file=genesis.json
kubectl create secret generic authority1-password --from-file=./authority1-password.txt
kubectl create secret generic authority2-password --from-file=./authority2-password.txt
```

## 3. Apply manifest files

```bash
kubectl apply -f bootnode.yaml
kubectl apply -f ethstats.yaml
kubectl apply -f authority1.yaml
kubectl apply -f authority2.yaml
```

## 4. Verify Ethereum network

```
kubectl port-forward <ethstats-pod-id> 3000:3000
```
Open your web browser and navigate to localhost:3000.
You should see that the authority nodes are mining blocks.


## FAQ

### Local setup with Minikube

Use nfs for the persistent volume to prevent permission errors:

##### Export the /Users directory as nfs from your host machine

```
echo "/Users -network 192.168.99.0 -mask 255.255.255.0 -alldirs -maproot=root:wheel" | sudo tee -a /etc/exports
sudo nfsd restart
```

##### Mount the /Users directory in the VM

```
minikube start
minikube ssh -- sudo umount /Users
minikube ssh -- sudo busybox mount -t nfs 192.168.99.1:/Users /Users -o nolock,tcp,rw
```
