# execute pkill on killmenow
exec { 'pkill -f killmenow':
    path     => ['/usr/bin', '/usr/sbin',],
}
