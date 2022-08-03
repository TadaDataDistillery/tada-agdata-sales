resource "aws_iam_policy" "agdata_sales_lambda_iam_policy" {
  name        = "${local.project}-lambda-iam-policy-${var.env}"
  description = "${local.project} policy for AWS Lambda"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:ListBucket",
          "s3:GetObject",
          "s3:DeleteObject",
          "s3:PutObject"
        ]
        Effect   = "Allow"
        Resource = [
          "${module.tada_agdata_sales_app_s3.s3_bucket_arn}",
          "${module.tada_agdata_sales_app_s3.s3_bucket_arn}/*"
        ]
      },
    ]
  })
  tags = merge(local.common_tags, tomap({
    "Name" = "${local.project}-lambda-iam-policy-${var.env}"
  }))
}

module "agdata_sales_report_lambda" {
  depends_on    = [null_resource.image_build, aws_ecr_repository.ecr_cbin]
  source        = "terraform-aws-modules/lambda/aws"
  runtime       = "python3.9"
  function_name = "${local.sales_report_lambda_name}-${var.env}"
  description   = "AgData Weekly Sales Report"
  image_config_command = ["handler.sales_report_handler"]
  image_uri            = "${local.base_ecr_url}:${local.image_data_version}"
  create_package       = false
  package_type         = "Image"
  memory_size          = 1024
  timeout              = 180
  #create_role    = false
  #lambda_role    = aws_iam_role.ingestion_lambda_execution_role.arn
  policy = aws_iam_policy.agdata_sales_lambda_iam_policy.id

  environment_variables = {
    RAW_PREFIX    = "${var.raw_data_path}"
    OUTPUT_PREFIX = "${var.output_data_path}"
    RAW_BUCKET    = "${local.project}-angus"
    OUTPUT_BUCKET = "${local.output_bucket}"
    STAGE         = "${var.env}"
  }
  tags = merge(local.common_tags, tomap({
    "Name" = local.sales_report_lambda_name
  }))
}
