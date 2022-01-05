# Puppet manifest that makes changes to the configuration file
include stdlib
file_line { '/etc/ssh/ssh_config':
  line =>  'PasswordAuthentication no',
}

file_line {  '/etc/ssh/ssh_config':
  line =>  'IdentityFile ~/.ssh/school',
}