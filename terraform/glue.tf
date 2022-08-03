resource "aws_iam_role" "glue_role" {
  name               = "${local.project}-glue-role-${var.env}"
  assume_role_policy = data.aws_iam_policy_document.glue_assume_role_policy.json
}

data "aws_iam_policy_document" "glue_assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["glue.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "glue_custom_policy" {
  statement {
    actions = [
      "s3:*",
    ]

    resources = [
      "${module.tada_agdata_sales_app_s3.s3_bucket_arn}",
      "${module.tada_agdata_sales_app_s3.s3_bucket_arn}/*",
      "${module.tada_agdata_grower_extract_app_s3.s3_bucket_arn}",
      "${module.tada_agdata_grower_extract_app_s3.s3_bucket_arn}/*",
      "arn:aws:s3:::${local.dataset_s3}/*",
      "arn:aws:s3:::${local.dataset_s3}"
    ]
  }
}

resource "aws_iam_role_policy" "glue_custom_policy" {
  name   = "${local.project}-glue_custom_policy"
  role   = aws_iam_role.glue_role.name
  policy = data.aws_iam_policy_document.glue_custom_policy.json
}

resource "aws_iam_role_policy_attachment" "glue_service_role_attachment" {
  role       = aws_iam_role.glue_role.name
  policy_arn = data.aws_iam_policy.glue_service_role.arn
}

data "aws_iam_policy" "glue_service_role" {
  arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}

resource "aws_glue_catalog_database" "agdata_glue_database" {
  name = "${local.project}_glue_database_${var.env}"
}

resource "aws_glue_crawler" "agdata_results_crawler" {
  database_name = aws_glue_catalog_database.agdata_glue_database.name
  name          = "${local.project}_results_crawler_${var.env}"
  role          = aws_iam_role.glue_role.arn
  configuration = jsonencode({
    "Version" : 1,
    "Grouping" : {
    "TableGroupingPolicy" : "CombineCompatibleSchemas" }
  })

  s3_target {
    path = "s3://${local.dataset_s3}/${local.dataset_glue_output_prefix}"
  }
}