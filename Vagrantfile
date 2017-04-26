# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 2 # added for increasing speed of execution
  end
  
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "mybase.yml"
    ansible.inventory_path = "dev"
    ansible.host_key_checking = false
    ansible.extra_vars = { 'ansible_connection' => 'ssh',
                           'ansible_ssh_args' => '-o ForwardAgent=yes'
                      	 }
    ansible.raw_ssh_args = ['-o UserKnownHostsFile=/dev/null', '-o StrictHostKeyChecking=false']
  end

  config.ssh.forward_agent = true
  config.vm.network "private_network", type: "dhcp"

  # Create a mybase machine 
  config.vm.define "mybase" do |mybase|
      mybase.vm.network :forwarded_port, host: 5000, guest: 5000 # gify-panda Flask port
      mybase.vm.network :forwarded_port, host: 5001, guest: 5001 # counter-panda Flask port
  end
end
