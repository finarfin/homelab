FROM roundcube/roundcubemail

COPY ca.crt /etc/ssl/certs/ca.pem
COPY php.ini /usr/local/etc/php/conf.d/php-customization.ini
COPY smtp-config.php /var/roundcube/config/smtp-config.php