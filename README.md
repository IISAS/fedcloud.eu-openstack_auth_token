# openstack_auth_token
Module for login into Horizon via Keystone token

#Installation instruction:

1. Requirements: Openstack Horizon installed and configured

2. Download the package: 
     "git clone https://github.com/tdviet/openstack_auth_token/"

3. Install: 
      "cd openstack_auth_token/; python setup.py install"

4. Copy template files to horizon: 
     "cp openstack_auth_token/templates/*  /usr/share/openstack-dashboard/horizon/templates/auth/"

5. Edit /etc/openstack-dashboard/local_settings.py and add following section:

AUTHENTICATION_URLS = [
    'openstack_auth.urls',
    'openstack_auth_token.urls',
]

6. Restart apache2 and open link https://$HORIZON_SERVER/horizon/auth/token/ in browser

#Use manual

1. Get keystone token from voms proxy. For convenience, you can download client tool 
     "git clone https://github.com/tdviet/Keystone-VOMS-client" 
to your machine with grid certificate (voms-proxy-* command should be there), and execute "./keystone-voms.sh"

2. open link https://$HORIZON_SERVER/horizon/auth/token/ in browser and copy/paste the issue token into input line






