# Puppet manifests that configures Nginx server

#Install nginx
package { 'nginx':
    ensure => installed,
}

#Create a page that contains the string Hellow World
file { '/var/www/html/index.html':
    content => 'Hellow World',
}

# Equivalent to the command service nginx restart
service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}