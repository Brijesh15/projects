FROM python:3.6-slim-buster as STAGE_1
RUN apt-get update && apt-get upgrade && apt-get install -y gcc make
WORKDIR /app
COPY . .
RUN ./install_udm_pre_req.sh
RUN apt-get -y remove gcc make
RUN apt-get -y autoremove

FROM STAGE_1
CMD ./start_udm.sh

