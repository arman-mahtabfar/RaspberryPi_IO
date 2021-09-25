FROM ubuntu:18.04

#resolve dependencies
RUN apt-get update && apt-get install cron -y && apt-get install python3 -y

#copy over the cron job
COPY ./container_cronjob /etc/cron.d/container_cronjob

#copy over the python file
COPY ./main.py /main.py

COPY ./start_cron.sh /script.sh
RUN chmod +x /script.sh

#start the program
CMD ["/bin/bash", "-c", "/script.sh && chmod 644 /etc/cron.d/container_cronjob && cron && tail -f /var/log/cron.log"]