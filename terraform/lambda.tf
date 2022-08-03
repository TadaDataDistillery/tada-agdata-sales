#module "tada_agdata_sales_report" {
#  depends_on    = [null_resource.image_build, aws_ecr_repository.ecr_cbin]
#  version       = "1.0.0"
#  source        = "terraform-aws-modules/lambda/aws"
#  runtime       = "python3.9"
#  function_name = "${local.sales_report_lambda_name}-${var.env}"
#  description   = "AgData Weekly Sales Report"
#  image_config_command = ["handler.sales_report"]
#  image_uri            = "${local.base_ecr_url}:${local.image_data_version}"
#  create_package       = false
#  package_type         = "Image"
#  memory_size          = 1024
#  timeout              = 180
#  
#  environment_variables = {
#    RAW_PREFIX    = "${var.raw_data_path}"
#    OUTPUT_PREFIX = "${var.output_data_path}"
#    RAW_BUCKET    = "${var.project}-angus"
#    OUTPUT_BUCKET = "${local.output_bucket}"
#    STAGE         = "${var.env}"
#  }
#  tags = merge(local.common_tags, tomap({
#    "Name" = "${local.tada_agdata_sales_name}-report"
#  }))
#}
