import requests
from kibanaSpaceManager import KibanaSpaceManager
kibanaSpaceManager = KibanaSpaceManager()
index_patterns = ('logstash-argocd-*','logstash-elastic-system-*','logstash-monitoring-*','logstash-cert-manager-*','logstash-kube-system-*','logstash-nginx-*')
space_name = 'devops'
kibanaSpaceManager.set_up_space(space_name,*index_patterns)
