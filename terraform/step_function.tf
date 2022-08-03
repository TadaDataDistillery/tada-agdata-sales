locals {
  wait_seconds                = 120
  job_starting_retry_attempts = 3
  step_function_definition    = <<EOF
{
  "Comment": "A description of my state machine",
  "StartAt": "Parallel",
  "States": {
    "Parallel": {
      "Type": "Parallel",
      "End": true,
      "Branches": [
        {
          "StartAt": "Lambda sales_report",
          "States": {
            "Lambda sales_report": {
              "Type": "Task",
              "Resource": "arn:aws:states:::lambda:invoke",
              "OutputPath": "$.Payload",
              "Parameters": {
                "FunctionName": "${module.agdata_sales_report_lambda.lambda_function_arn}"
              },
              "Retry": [
                {
                  "ErrorEquals": [
                    "Lambda.ServiceException",
                    "Lambda.AWSLambdaException",
                    "Lambda.SdkClientException"
                  ],
                  "IntervalSeconds": 2,
                  "MaxAttempts": 6,
                  "BackoffRate": 2
                }
              ],
              "End": true
            }
          }
        },
        {
          "StartAt": "Lambda grower_extract",
          "States": {
            "Lambda grower_extract": {
              "Type": "Task",
              "Resource": "arn:aws:states:::lambda:invoke",
              "OutputPath": "$.Payload",
              "Parameters": {
                "FunctionName": "${module.agdata_grower_extract_lambda.lambda_function_arn}"
              },
              "Retry": [
                {
                  "ErrorEquals": [
                    "Lambda.ServiceException",
                    "Lambda.AWSLambdaException",
                    "Lambda.SdkClientException"
                  ],
                  "IntervalSeconds": 2,
                  "MaxAttempts": 6,
                  "BackoffRate": 2
                }
              ],
              "End": true
            }
          }
        }
      ]
    }
  }
}
EOF
}

module "step_function" {
  source = "terraform-aws-modules/step-functions/aws"

  name       = "${var.project}-main-${var.env}"
  definition = local.step_function_definition

  service_integrations = {
    lambda = {
      lambda = [
        module.cbin_sales_report_lambda.lambda_function_arn,
        module.cbin_grower_extract_lambda.lambda_function_arn
      ]
    }
    tags = merge(local.common_tags, tomap({
    "Name" = "${var.project}-main-${var.env}"
  }))
  }
}