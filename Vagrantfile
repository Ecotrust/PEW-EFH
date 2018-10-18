# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrant::Config.run do |config|
Vagrant.configure("2") do |config|
    # Base box to build off, and download URL for when it doesn't exist on the user's system already
    config.vm.box = "ubuntu/trusty64"
    # config.vm.box = "p97-base-v0.4"
    # config.vm.box_url = "http://downloads.point97.io/p97-base-v0.4.box"
    # config.vm.hostname = "marine-planner"

    # Forward a port from the guest to the host, which allows for outside
    # computers to access the VM, whereas host only networking does not.
    # config.vm.forward_port 8000, 8000 # django dev server
    config.vm.network "forwarded_port", guest: 8000, host: 8000
    # config.vm.forward_port 8889, 8890 # mapproxy
    config.vm.network "forwarded_port", guest: 8889, host: 8890
    # config.vm.forward_port 5432, 15433 # postgresql
    config.vm.network "forwarded_port", guest: 5432, host: 15433

    # config.vm.customize [
    #   "modifyvm", :id,
    #   "--memory", "2048"
    # ]
    config.vm.provider "virtualbox" do |v|
      v.memory = 2048
      # v.cpus = 2
    end

    config.ssh.username = 'ubuntu'

    # config.vm.provider :virtualbox do |vb|
    #     vb.customize ["modifyvm", :id, "--memory", 256]
    # end

    # Share an additional folder to the guest VM. The first argument is
    # an identifier, the second is the path on the guest to mount the
    # folder, and the third is the path on the host to the actual folder.
    config.vm.synced_folder ".", "/usr/local/apps/PEW-EFH"

    # Enable provisioning with a shell script.
    # config.vm.provision :shell, :path => "scripts/vagrant_provision.sh"

    # If a 'Vagrantfile.local' file exists, import any configuration settings
    # defined there into here. Vagrantfile.local is ignored in version control,
    # so this can be used to add configuration specific to this computer.
    if File.exist? "Vagrantfile.local"
        instance_eval File.read("Vagrantfile.local"), "Vagrantfile.local"
    end
end
