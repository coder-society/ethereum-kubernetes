module "aws-production" {
  source = "github.com/poseidon/typhoon//aws/container-linux/kubernetes?ref=v1.10.2"

  providers = {
    aws = "aws.default"
    local = "local.default"
    null = "null.default"
    template = "template.default"
    tls = "tls.default"
  }

  cluster_name = "ethereum"
  dns_zone     = "blockchain.codersessions.com"
  dns_zone_id  = "Z2DIJCGE2FYL1N"

  ssh_authorized_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCe2BF0BhcACdt0gG34izY2NSYPlPFkpnv6J6p5dKX7lTeixSzohEhIiNdEmp1JCqOcXXikPSNkVthfAlGRLPXHWjdTTGXsoWE1MnsyI586UqSSvmaYJbuj8F9ZARcQmOZE344olZSZugICh3C78wvClUmI+ZZsZafqn4oigmxSaPRFv0H657+Ho7R4xVdulOvLxINl9/qGzrwTDWkStPsoFacQLl1d9Esq0fyFqXNt9PLcdWH0cVZ91QFPPg6KKm+azNxkxP8tU8G77W92FVGpnrtuDYjGKaht3UrXn/NTBXs33gNabRX0Xt/3ZXjfpI+cOZwMnE6neCOxTm+Lyo6N"
  asset_dir    = "${path.module}/assets"

  worker_type = "t2.small"
  worker_count = 3
  controller_count = 1
}
