# hello-world-ecs
Example repo: Flask hello-world instrumented with Prometheus, containerized, deployed to AWS ECS Fargate via Terraform, with GitHub Actions CI/CD.

## Quick local test
```bash
cd app
docker build -t hello-world-app:local .
docker run -p 8080:8080 hello-world-app:local
# visit http://localhost:8080 and http://localhost:8080/metrics
```

## Terraform (deploy to AWS)
1. Set AWS credentials in environment or GitHub secrets.
2. Edit terraform/variables.tf if you want a different region/name.
3. Run `terraform init`, `terraform plan`, `terraform apply` in the terraform/ folder.

## CI/CD
- Add GitHub secrets: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `ECR_REPO_NAME`.
- Push to `main` to trigger the workflow.

## Notes
- For production, configure Terraform remote state (S3 + DynamoDB) and use GitHub OIDC instead of long-lived keys.
- Clean up with `terraform destroy` to avoid charges.
# hello-world-devops
