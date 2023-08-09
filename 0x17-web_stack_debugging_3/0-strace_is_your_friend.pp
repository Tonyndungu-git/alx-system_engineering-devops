# replacing wrong file name with correct in wp-settings.php
exec{ 'fix-wordpress':
    command => 'sed -i \'s/class-wp-locale.phpp/class-wp-locale.php/g\' /var/ww\
w/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/',
}
