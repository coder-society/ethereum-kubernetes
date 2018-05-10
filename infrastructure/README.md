# Infrastructure
This subtree contains the configuration for bootstrapping our Kubernetes clusters on DigitalOcean,
for which we use [Typhoon](https://github.com/poseidon/typhoon), a Terraform module.

The various clusters are divided into corresponding directories, while common files are in
this directory.

## Add-Ons
Kubernetes add-ons to the cluster, i.e. additional components not installed by Typhoon, lie in the
'addons' directory.
