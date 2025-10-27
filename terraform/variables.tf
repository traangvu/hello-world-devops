variable "aws_region" {
  type    = string
  default = "eu-north-1"
}

variable "app_name" {
  type    = string
  default = "hello-world-app"
}

variable "desired_count" {
  type    = number
  default = 1
}
