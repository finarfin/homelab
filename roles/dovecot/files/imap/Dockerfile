FROM instrumentisto/dovecot:alpine

COPY ca.crt /etc/ssl/certs/ca.pem
COPY dovecot-ldap.conf.ext /etc/dovecot/dovecot-ldap.conf.ext
COPY dovecot-logging.conf /etc/dovecot/conf.d/dovecot-logging.conf
RUN sed -i -e 's,#!include auth-ldap.conf.ext,!include auth-ldap.conf.ext,' /etc/dovecot/conf.d/10-auth.conf

RUN mkdir /var/vmail \
 && addgroup -S -g 1001 vmail \
 && adduser -S -u 1001 -D -s /sbin/nologin \
            -H -h /var/vmail \
            -G vmail -g vmail vmail \
 && chown -R vmail:vmail /var/vmail
      