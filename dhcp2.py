from scapy.all import *

mac = str(RandMAC())
dhcpServerID="10.10.20.10"
eth = Ether(dst="ff:ff:ff:ff:ff:ff",src=mac)
ip  = IP(src="0.0.0.0",dst="255.255.255.255")
ud  = UDP(sport=68,dport=67)
bootp = BOOTP(chaddr=mac)
dhcp = DHCP(options = [ ("message-type","request"),("requested_addr","10.10.10.22"),("server_id",dhcpServerID),"end"])
sendp(eth/ip/ud/bootp/dhcp)
