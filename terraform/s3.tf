module "tada_agdata_sales_app_s3" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket = local.tada_agdata_sales_s3
  acl    = "private"

  versioning = {
    enabled = true
  }
  
  tags = merge(local.common_tags, tomap({
    "Name" = local.tada_agdata_sales_s3
  }))
}
