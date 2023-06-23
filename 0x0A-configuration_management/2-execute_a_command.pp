# execute kill command
exec { 'killmenow':
  command     => '/usr/bin/pkill killmenow',
  path        => '/usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
}
