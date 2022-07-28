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
```

The following handlers are used:

```
lambdas.settings.sales_report_handler
lambdas.settings.grower_extract_handler
```

File names are currently hardcoded within `lambdas/handler.py` but these can moved into configurable environment variables if required in the future.
