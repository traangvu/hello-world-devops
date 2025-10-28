terraform {
  backend "s3" {
    bucket        = "tfstate-628651171723-eu-north-1"
    key           = "hello-world-ecs/terraform.tfstate"
    region        = "eu-north-1"
    encrypt       = true
    use_lockfile  = true
  }
}

