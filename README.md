# AgData Weekly Sales Report

## Development

1. Change into `src/`
2. Create new virtual environment: `virtualenv venv -p python3.8`
3. Activate virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r dev_requirements.txt -r requirements.txt`
5. Populate test data:
```
mkdir -p data/raw
mkdir -p data/output/sales_report
mkdir -p data/output/grower_extract
cp [path to grower extract] data/raw/grower-extract-small.xlsx
cp [path to sales report] data/raw/sales-report-small.xlsx
```
6. Run syntax checks and tests: `make all`

## Deployment

To run in AWS, environment variables must be set to define S3 buckets and paths. These are loaded in `lambdas/settings.py` and are:

```
RAW_BUCKET  # bucket storing raw xlsx files
RAW_PREFIX  # path within raw bucket
OUTPUT_BUCKET  # bucket to store output datasets
OUTPUT_PREFIX  # path within output bucket
STAGE  # dev, prod, etc.
```

The following handlers are used:

```
lambdas.settings.sales_report_handler
lambdas.settings.grower_extract_handler
```

The `awswrangler` dependency may be too large for a standard zip install within a Lambda - if so, the optimized layer release zip can be used intead from here: https://github.com/awslabs/aws-data-wrangler/releases

File names are currently hardcoded within `lambdas/handler.py` but these can moved into configurable environment variables if required in the future.

Invocation can be manual initially and will expect correctly named files in the location specified by environment variables. This can be updated in the future when/if necessary.


## Terraform Deployments
TA-DA Data Distillery

### Requirements
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

### Deployment

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

### Removal

To remove this deployment, ensure your variables are set, validate the templates and ensure no changes are found in the plan stage. Then you can run the "destroy" command as follows. Some additional manual steps may be required in some cases, so please read the output carefully.

```bash
terraform destroy --auto-approve -var-file=envs/${ENV}.tfvars
```