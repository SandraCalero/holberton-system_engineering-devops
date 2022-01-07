# Puppet manifests that configures Nginx server
package { 'nginx':
    ensure => installed,
}

service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}