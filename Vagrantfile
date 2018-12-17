# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  # config.vm.forward_port 8889, 8890 # mapproxy
  config.vm.network "forwarded_port", guest: 8889, host: 8890
  # config.vm.forward_port 5432, 15433 # postgresql
  config.vm.network "forwarded_port", guest: 5432, host: 15433

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    # v.cpus = 2
  end

  # config.ssh.username = 'ubuntu'

  config.vm.synced_folder ".", "/usr/local/apps/PEW-EFH"

  if File.exist? "Vagrantfile.local"
      instance_eval File.read("Vagrantfile.local"), "Vagrantfile.local"
  end

end
