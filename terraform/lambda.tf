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
          "*",
          "*/*"
          #"${module.tada_agdata_sales_app_s3.s3_bucket_arn}",
          #"${module.tada_agdata_sales_app_s3.s3_bucket_arn}/*",
          #"${module.tada_agdata_grower_extract_app_s3.s3_bucket_arn}",
          #"${module.tada_agdata_grower_extract_app_s3.s3_bucket_arn}/*"
        ]
      },
    ]
  })
  tags = merge(local.common_tags, tomap({
    "Name" = "${local.project}-lambda-iam-policy-${var.env}"
  }))
}

module "agdata_sales_report_lambda" {
  depends_on    = [null_resource.image_build, aws_ecr_repository.lambda_ecr]
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
    RAW_BUCKET    = "${local.sales_report_lambda_s3}"
    RAW_PREFIX    = "${local.sales_report_lambda_input_prefix}"
    OUTPUT_BUCKET = "${local.sales_report_lambda_s3}"
    OUTPUT_PREFIX = "${local.sales_report_lambda_output_prefix}"
    STAGE         = "${var.env}"
  }
  tags = merge(local.common_tags, tomap({
    "Name" = local.sales_report_lambda_name
  }))
}

module "agdata_grower_extract_lambda" {
  depends_on    = [null_resource.image_build, aws_ecr_repository.lambda_ecr]
  source        = "terraform-aws-modules/lambda/aws"
  runtime       = "python3.9"
  function_name = "${local.grower_extract_lambda_name}-${var.env}"
  description   = "AgData Grower Exctract"
  image_config_command = ["handler.grower_extract_handler"]
  image_uri            = "${local.base_ecr_url}:${local.image_data_version}"
  create_package       = false
  package_type         = "Image"
  memory_size          = 1024
  timeout              = 180
  #create_role    = false
  #lambda_role    = aws_iam_role.ingestion_lambda_execution_role.arn
  policy = aws_iam_policy.agdata_sales_lambda_iam_policy.id

  environment_variables = {
    RAW_BUCKET    = "${local.grower_extract_lambda_s3}"
    RAW_PREFIX    = "${local.grower_extract_lambda_input_prefix}"
    OUTPUT_BUCKET = "${local.grower_extract_lambda_s3}"
    OUTPUT_PREFIX = "${local.grower_extract_lambda_output_prefix}"
    STAGE         = "${var.env}"
  }
  tags = merge(local.common_tags, tomap({
    "Name" = local.grower_extract_lambda_name
  }))
}



#process_sheets