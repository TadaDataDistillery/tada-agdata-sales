data "aws_caller_identity" "current" {}

locals{
  project = "tada-agdata-sales"
  tada_releases_s3 = "tada-releases-${var.env}"
  sales_report_lambda_name = "tada-agdata-sales-report"
  sales_report_lambda_s3 = "${local.sales_report_lambda_name}-app-${var.env}"
  sales_report_lambda_input_prefix = "/input"
  sales_report_lambda_output_prefix = "/output"
  base_ecr_url = ""
  image_data_version = ""

  common_tags = {
    Project     = local.project
    Environment = var.env
    CreatedBy   = "Terraform"
    Terraform   = true
    Owner       = var.owner_tag
  } 
}

module security {
  source = "./modules/security"
  env = var.env
  region = var.region
  common_tags = local.common_tags
  project = local.project
  sales_report_lambda_s3 = local.sales_report_lambda_s3
}
