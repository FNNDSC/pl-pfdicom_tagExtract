# Docker file for the dcm_tagExtract plugin app

FROM fnndsc/ubuntu-python3:latest
MAINTAINER fnndsc "dev@babymri.org"

ENV APPROOT="/usr/src/dcm_tagExtract"  VERSION="0.1"
COPY ["dcm_tagExtract", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]

WORKDIR $APPROOT

RUN pip install -r requirements.txt

CMD ["dcm_tagExtract.py", "--help"]