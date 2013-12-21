# OpenShift Nginx + Python Cartridge

This cartridge adds support to run python 2.7/3.3 under OpenShift, using nginx as a reverse proxy and static files server.

Create your app:

```
$ rhc app create myapp https://reflector-getupcloud.getup.io/reflect?github=caruccio/openshift-nginx-python
```

Place static files under `wsgi/static` than push. Nginx config is `config/nginx.d/default.conf.erb` (or whatever you want to put in config/nginx.d/).

Note: By using downloadable cartridges (the example above) it works only with python-2.7 since there is no way to choose python version during app creation. You must install it under you own openshift installation to be able to use python-3.3. If you need help, please fell free to contact me.
