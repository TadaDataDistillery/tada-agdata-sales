#IAM Policy Outputs
#id
#arn
#name
#policy
output "lambda_agdata_sales_iam_policy_id" {
  description = "AWS IAM Policy ID"
  value       = aws_iam_policy.lambda_agdata_sales_iam_policy.id
}
