# issue fixing for files i/o
exec {'fd':
path     => ['/usr/bin', '/bin'],
command  => "sudo sed -i 's/15/3000/g' /etc/default/nginx; sudo service nginx r\
estart",
provider => 'shell',
}
