FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY data_unification data_unification
COPY lambdas lambdas
COPY lambdas/handler.py .

# handler chosen during Lambda creation
# CMD ["handler.sales_report_handler"]