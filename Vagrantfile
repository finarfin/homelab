Vagrant.configure("2") do |config|
  node_name = "docker"
  node_ip = "192.168.5.2"
  config.vm.box = "ubuntu/bionic64"       
  config.vm.host_name = node_name
  config.vm.network "private_network", ip: node_ip
  config.vbguest.auto_update = false
  config.vm.provider 'virtualbox' do |vbox|
    vbox.name = node_name
    vbox.memory = 4096
    vbox.cpus = 4
    vbox.customize ["modifyvm", :id, "--uartmode1", "disconnected"]
    
    vdisk_name = ".vagrant/#{node_name}.vdi"
    unless File.exist?(vdisk_name)
       vbox.customize ['createhd', '--filename', vdisk_name, '--size', "#{10*1024}"]
    end
    vbox.customize ['storageattach', :id, '--storagectl', "SCSI", '--port', 2, '--device', 0, '--type', 'hdd', '--medium', vdisk_name]        
  end   

  config.vm.provision "docker"
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "playbook.yml"
  end      
end
