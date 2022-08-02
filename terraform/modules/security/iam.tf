resource "aws_iam_policy" "lambda_agdata_sales_iam_policy" {
  name        = "agdata-sales-iam-policy-${var.env}"
  description = "agdata-sales policy for AWS Lambda"

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
          "arn:aws:s3:::${var.tada_agdata_sales_s3}",
          "arn:aws:s3:::${var.tada_agdata_sales_s3}/*"
        ]
      },
    ]
  })
  tags = merge(var.common_tags, tomap({
    "Name" = "agdata-sales-iam-policy-${var.env}"
  }))
}