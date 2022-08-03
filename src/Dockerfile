FROM public.ecr.aws/lambda/python:3.8

COPY ../src/requirements.txt .
RUN pip install -r requirements.txt

COPY data_unification data_unification
COPY ../src/lambdas lambdas
COPY ../src/lambdas/handler.py .

# handler chosen during Lambda creation
# CMD ["handler.sales_report_handler"]