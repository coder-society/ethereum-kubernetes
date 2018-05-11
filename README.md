# Setup a permissioned Ethereum blockchain on Kubernetes

## Prerequisites

### envsubst

You will need envsubst for generating the Kubernetes manifest files.
It's part of the gettext package which you can install e.g. with homebrew on macOS:

```bash
brew install gettext
brew link --force gettext
```

### kubectl

We also need [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/). You can also install with homebrew:

```bash
brew install kubectl
```

### Kubernetes cluster

We need a Kubernetes cluster. Locally we stick with [Minikube](https://github.com/kubernetes/minikube) and in the cloud we use our self-rolled [cluster on AWS](https://github.com/coder-society/k8s-aws/).

#### Local setup

You can install Minikube with homebrew:

```bash
brew cask install minikube
```

Start Minikube and create the StorageClass which we will need later:

```bash
minikube start --memory 5120 --cpus=4
kubectl apply -f minikube-general-storageclass.yaml
```

#### Cloud setup

As for the cloud, we use AWS. In order to bootstrap and administrate clusters on AWS we use the
[kops](https://github.com/kubernetes/kops) tool, although via our opinionated wrapper
[k8s-aws](https://github.com/coder-society/k8s-aws/).

## 1. Generate Kubernetes manifest files

In order to generate our Kubernetes manifests, beneath kubernetes/, run `./generate-manifests.py`.

## 2. Apply manifest files

```bash
./kubectl apply -f kubernetes/
```

## 3. Verify Ethereum network

```
./kubectl port-forward <ethstats-pod-id> 3000:3000
```
Open your web browser and navigate to localhost:3000.
You should see that the authority nodes are mining blocks.

## 4. Delete Kubernetes resources

Once you are done, you can delete the Kubernetes resources:

```bash
./kubectl delete -f kubernetes/
```

To fully delete the blockchain you also need to delete the geth folders in the authority1
and authority2 directories.

## 5. Learn more

Learn more about Coder Society, a network of cutting edge developers, designers and product engineers at https://codersociety.com
