# base image
FROM python:3.11-slim

# install all required libraries
RUN pip install --no-cache-dir pandas numpy matplotlib seaborn scikit-learn scipy requests

# set working directory inside container
WORKDIR /app/pipeline/

# copy everything into the container
COPY . /app/pipeline/

# open shell when container starts
CMD ["/bin/bash"]