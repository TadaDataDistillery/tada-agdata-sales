data "aws_caller_identity" "current" {}

locals{
  project = "tada-agdata-sales"
  depends_on = [module.vpc]
  vpc_id = var.create_vpc ? module.vpc.vpc_id : var.vpc_id
  subnet_ids = var.create_vpc ? module.vpc.private_subnets : var.private_subnets_ids
  public_subnet_ids = var.create_vpc ? module.vpc.public_subnets : var.public_subnets_ids

  tada_releases_s3 = "tada-releases-${var.env}"
  sales_report_lambda_name = "tada-agdata-sales-report"
  sales_report_lambda_s3 = "${local.sales_report_lambda_name}-app-${var.env}"
  sales_report_lambda_input_prefix = "/input"
  sales_report_lambda_output_prefix = "/output"

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
