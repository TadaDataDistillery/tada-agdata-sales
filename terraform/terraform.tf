terraform {
  backend "s3" {}
}

provider "aws" {
  region  = var.region
}

data "aws_caller_identity" "current" {}

data "aws_iam_session_context" "current" {
  arn = data.aws_caller_identity.current.arn
}

data "aws_region" "current" {}
