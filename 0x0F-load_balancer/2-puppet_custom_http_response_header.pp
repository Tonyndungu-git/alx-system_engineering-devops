# Install Nginx package
package { 'nginx':
  ensure => installed,

}

# create nginx configuration with custom header
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => present,
  content => "add_header X-Served-By $hostname;",
  require => Package['nginx'],
  notify  => Service['nginx'],

}

# configure nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/conf.d/custom_header.conf'],
}
