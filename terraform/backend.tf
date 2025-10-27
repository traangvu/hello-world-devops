terraform {
  backend "s3" {
    bucket       = "tf-state-628651171723-prod"
    key          = "hello-world-devops/terraform.tfstate"
    region       = "eu-north-1"
    use_lockfile = true
    encrypt      = true
  }
}
