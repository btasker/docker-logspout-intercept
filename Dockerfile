FROM python

ENV PYTHONUNBUFFERED=1
RUN pip3 install scapy docker \
&& apt-get update \
&& apt-get -y install libpcap0.8 \ 
&& apt-get clean autoclean \
&& apt-get -y autoremove \
&& rm -rf /var/lib/apt/lists

COPY app /app/

ENTRYPOINT ["/app/capture_and_print.py"]

