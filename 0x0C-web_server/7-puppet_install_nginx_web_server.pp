# Puppet manifests that configures Nginx server
include nginx

nginx::resource::server { 'ubuntu.35.196.20.175':
  listen_port => 80,
  proxy       => 'http://localhost:5601',
}
