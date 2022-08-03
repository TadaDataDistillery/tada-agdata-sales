data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

locals{
  # Project settings
  project = "tada-agdata-sales"
  image_major_version = "0"
  image_minor_version = "1"
  image_patch_version = format("%s-%s-%s", "local", local.image_major_version, local.image_minor_version)
  image_data_version = "image_${local.image_major_version}.${local.image_minor_version}.${local.image_patch_version}"
  ecr_address        = format("%v.dkr.ecr.%v.amazonaws.com", data.aws_caller_identity.current.account_id, data.aws_region.current.name)
  base_ecr_url       = "${local.ecr_address}/${local.project}-lambda-ecr-${var.env}"
  
  # Lambda Configuration
  sales_report_lambda_name          = "${local.project}-report"
  sales_report_lambda_s3            = "${local.sales_report_lambda_name}-app-${var.env}"
  sales_report_lambda_input_prefix  = "/raw"
  sales_report_lambda_output_prefix = "/processed"
  grower_extract_lambda_name          = "${local.project}-grower-extract"
  grower_extract_lambda_s3            = "${local.grower_extract_lambda_name}-app-${var.env}"
  grower_extract_lambda_input_prefix  = "/raw"
  grower_extract_lambda_output_prefix = "/processed"


  # Global tagging defaults
  common_tags = {
    Project     = local.project
    Environment = var.env
    CreatedBy   = "Terraform"
    Terraform   = true
    Owner       = var.owner_tag
  } 
}
