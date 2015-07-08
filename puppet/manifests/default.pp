# basic bootstrap
exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
}

# basic bootstrap
exec { 'apt-get upgrade -y':
  command => '/usr/bin/apt-get upgrade -y'
}

# pacotes basicos
$enhancers = [ "git-core", "screen", "python-psycopg2", "libpq-dev", "freetds-dev", "libmysqlclient-dev",  "libjpeg-dev", "libfreetype6-dev", "zlib1g-dev", "libpng12-dev"]
package { 
  $enhancers: ensure => "installed"
}

class { 'postgresql::server':
  ip_mask_allow_all_users    => '0.0.0.0/0',
  listen_addresses           => '*',
}

postgresql::server::role { 'llm':
  password_hash => postgresql_password('llm', 'llm'),
  createdb  => true
}

postgresql::server::db { 'llm':
  user     => 'llm',
  password => postgresql_password('llm', 'llm'),
}

postgresql::server::database_grant { 'llm':
  privilege => 'ALL',
  db        => 'llm',
  role      => 'llm',
}

postgresql::server::pg_hba_rule { 'permite acesso local para usuario':
  description => "permite acesso local para usuario",
  type => 'local',
  database => 'llm',
  user => 'llm',
  auth_method => 'md5',
  order=>'001',
}


# Install & configure Python
class { 'python' :
  virtualenv => true,
  dev        => true,
}

# Create the directory where the app will be installed
file { '/opt/llm/source/':
  ensure => directory,
}

# Create a virtualenv and install deps
python::virtualenv { '/opt/llm/virtualenv' :
    ensure       => present,
    version      => 'system',
    requirements => '/opt/llm/source/requirements.txt',
    systempkgs   => false,
    distribute   => false,
    owner        => 'vagrant',
    group        => 'vagrant',
    timeout      => 0,
  }