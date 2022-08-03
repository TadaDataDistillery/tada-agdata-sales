locals {
  user                     = data.aws_iam_session_context.current.issuer_arn
  data_product_bucket      = "${local.project}-data-product-${var.env}"
  lakeformation_admin_role = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:role/aws-reserved/sso.amazonaws.com/${var.region}/AWSReservedSSO_AWSPowerUserAccess_${var.SSOPowerUserId}"
  main_admin_role          = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:role/aws-reserved/sso.amazonaws.com/${var.region}/AWSReservedSSO_AWSAdministratorAccess_${var.SSOAdminUserId}"
}

resource "aws_lakeformation_resource" "sales_report" {
  arn = "arn:aws:s3:::${local.grower_extract_lambda_s3}"
}

resource "aws_lakeformation_resource" "grower_extract" {
  arn = "arn:aws:s3:::${local.sales_report_lambda_s3}"
}

resource "aws_lakeformation_resource" "data_product" {
  arn = "arn:aws:s3:::${local.dataset_s3}"
}

resource "aws_lakeformation_data_lake_settings" "data_lake_settings" {
  depends_on = [data.aws_iam_session_context.current]
  admins     = [data.aws_iam_session_context.current.issuer_arn, local.lakeformation_admin_role, local.main_admin_role]
}

resource "aws_lakeformation_permissions" "glue_db_permissions" {
  principal   = data.aws_iam_session_context.current.issuer_arn
  permissions = ["CREATE_TABLE", "ALTER", "DROP"]

  database {
    name       = aws_glue_catalog_database.agdata_glue_database.name
    catalog_id = aws_glue_catalog_database.agdata_glue_database.catalog_id
  }
}

resource "aws_lakeformation_permissions" "sales_report_s3_permissions" {
  principal   = aws_iam_role.glue_role.arn
  permissions = ["DATA_LOCATION_ACCESS"]

  data_location {
    arn = aws_lakeformation_resource.sales_report.arn
  }
}

resource "aws_lakeformation_permissions" "grower_extract_s3_permissions" {
  principal   = aws_iam_role.glue_role.arn
  permissions = ["DATA_LOCATION_ACCESS"]

  data_location {
    arn = aws_lakeformation_resource.grower_extract.arn
  }
}

resource "aws_lakeformation_permissions" "data_product_s3_permissions" {
  principal   = aws_iam_role.glue_role.arn
  permissions = ["DATA_LOCATION_ACCESS"]

  data_location {
    arn = aws_lakeformation_resource.data_product.arn
  }
}