# Fix 500 internal server error .phpp to .php
exec {'fixApache':
      command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
      path    => '/bin/',
}
