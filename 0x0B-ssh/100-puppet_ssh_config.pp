# Puppet manifest that makes changes to the configuration file
include stdlib
file_line { 'Set PasswordAuthentication':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
}

file_line { 'Add IdentityFile to use the private key ~/.ssh/school':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school',
}
