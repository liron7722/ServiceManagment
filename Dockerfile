FROM ubuntu
RUN apt-get update && apt-get install -y --no-install-recommends git python3 python3-pip python3-venv
RUN git clone -b Production https://github.com/liron7722/ServiceManagment.git
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR ServiceManagment
RUN pip install -r req.txt
CMD [ "python3", "./main.py" ]