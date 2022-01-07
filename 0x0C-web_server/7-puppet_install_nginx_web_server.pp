# Puppet manifests that configures Nginx server
exec { 'sudo apt-get -y update':
    path    => '/usr/bin/',
}

exec { 'sudo apt-get -y install nginx':
    path    => '/usr/bin/',
}

exec { 'sudo ufw allow 'Nginx HTTP'':
    path    => '/usr/bin/',
}

exec { 'echo "Hello World" > /var/www/html/index.html':
    path    => '/usr/bin/',
}

exec { 'new_page="https://www.youtube.com/watch?v=QH2-TGUlwu4"':
    path    => '/usr/bin/',
}
exec { 'file="/etc/nginx/sites-available/default"':
    path    => '/usr/bin/',
}
exec { 'sudo sed -i "/listen 80 default_server/a rewrite ^/redirect_me $new_page permanent;" $file':
    path    => '/usr/bin/',
}

exec { 'sudo service nginx restart':
    path    => '/usr/bin/',
}
