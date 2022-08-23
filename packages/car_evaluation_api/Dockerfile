FROM python:3.9.4

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/car_evaluation_api

ARG PIP_EXTRA_INDEX_URL

# Install requirements, including from Gemfury
ADD ./car_evaluation_api /opt/car_evaluation_api
RUN pip install --upgrade pip
RUN pip install -r /opt/car_evaluation_api/requirements.txt

RUN chmod +x /opt/car_evaluation_api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
