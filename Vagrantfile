Vagrant.configure("2") do |config|
  node_name = "docker"
  node_ip = "192.168.5.2"
  config.vm.box = "ubuntu/bionic64"       
  config.vm.host_name = node_name
  config.vm.network "private_network", ip: node_ip
  config.vbguest.auto_update = false
  config.vm.provider 'virtualbox' do |vbox|
    vbox.name = node_name
    vbox.memory = 8192
    vbox.cpus = 4
    vbox.customize ["modifyvm", :id, "--uartmode1", "disconnected"]
    
    vdisk_name = ".vagrant/#{node_name}.vdi"
    unless File.exist?(vdisk_name)
       vbox.customize ['createhd', '--filename', vdisk_name, '--size', "#{30*1024}"]
    end
    vbox.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vbox.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    vbox.customize ['storageattach', :id, '--storagectl', "SCSI", '--port', 2, '--device', 0, '--type', 'hdd', '--medium', vdisk_name]        
  end   

  config.vm.provision "docker"
  config.vm.provision "ansible_local" do |ansible|
    ansible.install_mode = :pip
    ansible.version = "2.6.4"
    ansible.playbook_command = "ANSIBLE_FORCE_COLOR=true ansible-playbook"
    ansible.playbook = "playbook.yml"
  end      
end
