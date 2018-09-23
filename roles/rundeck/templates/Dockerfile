FROM rundeck/rundeck:3.0.6

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends python-pip python-setuptools \
  && rm -rf /var/lib/apt/lists/* \
  && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
  && apt-get clean

RUN pip install --upgrade pip
RUN pip install ansible

USER rundeck

RUN echo "rundeck.tokens.file=/home/rundeck/etc/tokens.properties" >> /etc/remco/templates/framework.properties  
RUN mkdir -p /home/rundeck/libext
{% for plugin in RUNDECK_PLUGINS %}
RUN curl -sfL -o /home/rundeck/libext/{{ plugin | urlsplit('path') | basename }} {{ plugin }}
{% endfor %}