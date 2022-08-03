# data-distillery
TA-DA Data Distillery

## Requirements
* [terraform](https://www.terraform.io/downloads) - AWS Infrastructure Automation
* [tfenv](https://github.com/tfutils/tfenv) - Terraform version manager

### Variables

Export the AWS CLI credentials from Control Tower (likeley the "PowerUser"), or otherwise configure and test your AWS CLI before the next steps.

Declare the environment and primary region that you will be deploying into.

```bash
export ENV="sandbox"
export AWS_REGION="us-east-1"
export PROJECT="tada-agdata-sales"
```

## Deployment

Once your environment variables are configure, we can initialize our Terraform deployment.

```bash
terraform init \
-upgrade \
-backend-config="bucket=${PROJECT}-tfstate-${AWS_REGION}-${ENV}" \
-backend-config="key=${ENV}/project-infra.tfstate" \
-backend-config="region=${AWS_REGION}"
```

Validate your template syntax against the initialized environment. Fix any errors you find here, before moving to the next step.

```bash
terraform validate
```

Show the proposed changes to the AWS Account, and ensure that your changes look good.

```bash
terraform plan -var-file=envs/${ENV}.tfvars
```

Once your environment is initialized and validated, and the proposed changes have been verified, you are finally ready to deploy!

```bash
terraform apply --auto-approve -var-file=envs/${ENV}.tfvars
```

## Removal

To remove this deployment, ensure your variables are set, validate the templates and ensure no changes are found in the plan stage. Then you can run the "destroy" command as follows. Some additional manual steps may be required in some cases, so please read the output carefully.

```bash
terraform destroy --auto-approve -var-file=envs/${ENV}.tfvars
```