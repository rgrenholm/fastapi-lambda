FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY api.py api.py
COPY plant_classifier.py plant_classifier.py

CMD ["api.handler"]
