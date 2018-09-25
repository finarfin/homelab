FROM jenkins/jenkins:lts

USER root
RUN apt-get update -qq \
    && apt-get install -qqy apt-transport-https ca-certificates curl gnupg2 software-properties-common 
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"
RUN apt-get update  -qq \
    && apt-get install docker-ce=17.12.1~ce-0~debian -y
RUN usermod -aG docker jenkins

ARG JAVA_OPTS
ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false -Dmail.smtp.starttls.enable=true -Dmail.smtp.ssl.protocols=TLSv1.2 -Djava.util.logging.loglevel=FINE ${JAVA_OPTS:-}"

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN xargs /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

ENV CASC_JENKINS_CONFIG=/var/jenkins_home/casc_configs/jenkins.yaml
COPY config.yml /var/jenkins_home/casc_configs/jenkins.yaml

COPY ca.crt $JAVA_HOME/jre/lib/security
RUN cd $JAVA_HOME/jre/lib/security \
    && keytool -keystore cacerts -storepass changeit -noprompt -trustcacerts -importcert -alias ldapcert -file ca.crt

RUN echo ${JENKINS_VERSION:-2.0} > /var/jenkins_home/jenkins.install.InstallUtil.lastExecVersion