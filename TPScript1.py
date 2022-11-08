#!/usr/bin/fr python
# -*- coding: utf-8 -*-
import socket

# Retourner adresse locale et publique
NomHost = socket.gethostname()
HOST = socket.gethostbyname(socket.gethostname())
print("Hostname : {}".format(NomHost))
print("Adresse IP : {}".format(HOST))

# Affiche adresse IP des DNS
dns_client1 = "facebook.fr"
dns_client2 = "google.fr"

ip_dns1 = socket.gethostbyname(dns_client1)
ip_dns2 = socket.gethostbyname(dns_client2)

print("adresse serveur DNS de {} : {}".format(dns_client1, ip_dns1))
print("adresse serveur DNS de {} : {}".format(dns_client2, ip_dns2))

# Affiche les FQDN
f_client1 = "yahoo.fr"
f_client2 = "google.fr"
f_client3 = "steams.fr"

fqdn1 = socket.getfqdn(f_client1)
fqdn2 = socket.getfqdn(f_client2)
fqdn3 = socket.getfqdn(f_client3)

print("adresse FQDN de {} : {}".format(f_client1, fqdn1))
print("adresse FQDN de {} : {}".format(f_client2, fqdn2))
print("adresse FQDN de {} : {}".format(f_client3, fqdn3))

# adresses info + FQDN
i_client1 = "yahoo.fr"
i_client2 = "google.fr"

info_client1 = socket.getaddrinfo(i_client1, 80, proto=socket.IPPROTO_TCP)
info_client2 = socket.getaddrinfo(i_client2, 80, proto=socket.IPPROTO_TCP)

print("adresse FQDN de {} : {}".format(f_client1, fqdn1))
print(info_client1)

print("adresse FQDN de {} : {}".format(f_client2, fqdn2))
print(info_client2)
