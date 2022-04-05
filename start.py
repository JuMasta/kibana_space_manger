import requests
from kibanaSpaceManager import KibanaSpaceManager
# USER = 'elastic'
# PASSWORD = 'AGXM4buRzrqYYJk8WXxnPwdX'
# KIBANA_URL = 'https://virtoway-learning.kb.us-central1.gcp.cloud.es.io'
# AUTH_DATA = ( USER, PASSWORD )
# POST_HEADERS = {'Content-Type':'application/json', 'kbn-xsrf' : 'true'}
#
#
# space_id = 'devops'
# space_name = 'DevOps'
# space_description = 'This is your DevOps logs'
# space_attributes = {
#     	"id": space_id,
#     	"name": space_name,
#     	"description": space_description,
#     	"disabledFeatures": []
#     }
#
# def create_space(space_attributes):
#
#     CREATE_SPACE_API = '/api/spaces/space'
#     space_response = requests.get( KIBANA_URL + CREATE_SPACE_API,
#                              auth=AUTH_DATA,
#                              headers=POST_HEADERS,
#                              json=space_attributes)
#     print(space_response.text)
#     if space_response.status_code != 200:
#         raise Exception(space_response.text)
#
#
#
#
#
# index_pattern_attributes = {
#     "index_pattern" : { "title": "argocd-*" }
# }
#
#
# def create_index_pattern(index_pattern_attributes):
#     CREATE_INDEX_PATTERN_API = '/s/' + space_id + '/api/index_patterns/index_pattern'
#     index_pattern_response = requests.post( KIBANA_URL + CREATE_INDEX_PATTERN_API,
#                     auth=AUTH_DATA ,
#                     headers=POST_HEADERS,
#                     json=index_pattern_attributes)
#
#
#     if index_pattern_response.status_code != 200:
#         raise Exception(index_pattern_response.text)
#
#
#
#
# def get_dashboards():
#     GET_DASHBOARD_API = '/s/' + space_id + '/api/saved_objects/_find?type=dashboard'
#     r = requests.get(KIBANA_URL + GET_DASHBOARD_API,
#                      auth=AUTH_DATA )
#     print(r.json()['saved_objects'][0])
#
# # get_dashboards()
# dashboard_attributes = {
#     "attributes" :
#     {
#      'title': 'Devops-Dashboard',
#      'hits': 0, 'description':
#      'This is your DevOps-Dashboard',
#      'panelsJSON': '[{\"gridData\":{\"w\":24,\"h\":15,\"x\":0,\"y\":0,\"i\":\"1\"},\"version\":\"7.0.0-alpha1\",\"panelIndex\":\"1\",\"type\":\"visualization\",\"id\":\"argocd-timeseries\",\"embeddableConfig\":{}},' +
#                     '{\"gridData\":{\"w\":24,\"h\":15,\"x\":0,\"y\":0,\"i\":\"2\"},\"version\":\"7.0.0-alpha1\",\"panelIndex\":\"2\",\"type\":\"visualization\",\"id\":\"elastic-system-timeseries\",\"embeddableConfig\":{}}]',
#      'optionsJSON': '{"useMargins":true,"syncColors":false,"hidePanelTitles":false}',
#      'version': 1,
#      'timeRestore': False,
#      'kibanaSavedObjectMeta': {'searchSourceJSON': '{"query":{"query":"","language":"kuery"},"filter":[]}'}}
# }
#
# def create_dashboard(dashboard_attributes):
#     CREATE_DASHBOARD_API = '/s/' + space_id + '/api/saved_objects/dashboard/DevOps-Dashboard'
#     r = requests.post( KIBANA_URL + CREATE_DASHBOARD_API,
#                      auth=AUTH_DATA,
#                      headers=POST_HEADERS,
#                      json=dashboard_attributes )
#     print(r.json())
#
#
#
#
# # create_dashboard(dashboard_attributes)
#
# visualization_attributes = {
#     'attributes':
#     {
#         'visState': '{"title":"Elastic","type":"metrics","aggs":[],"params":{"time_range_mode":"entire_time_range","id":"77993351-2b37-42b4-8e9f-7d8211a3924d","type":"timeseries","series":[{"time_range_mode":"entire_time_range","id":"df2052f9-a74a-4a2e-b807-aa56dfbcfad0","color":"#68BC00","split_mode":"terms","palette":{"type":"palette","name":"default"},"metrics":[{"id":"fff3f0e7-86b5-49e3-9553-309ef034d266","type":"count"}],"separate_axis":0,"axis_position":"right","formatter":"default","chart_type":"line","line_width":1,"point_size":1,"fill":0.5,"stacked":"none","override_index_pattern":0,"series_drop_last_bucket":0,"terms_field":"level.keyword"}],"time_field":"@timestamp","use_kibana_indexes":true,"interval":"","axis_position":"left","axis_formatter":"number","axis_scale":"normal","show_legend":1,"truncate_legend":1,"max_lines_legend":1,"show_grid":1,"tooltip_mode":"show_all","drop_last_bucket":0,"annotations":[{"id":"783326c0-af52-11ec-a74e-1f946bbc3008","color":"#F00","time_field":"@timestamp","icon":"fa-tag","ignore_global_filters":1,"ignore_panel_filters":1,"index_pattern_ref_name":"metrics_1_index_pattern"}],"isModelInvalid":false,"index_pattern_ref_name":"metrics_0_index_pattern"}}', 'title': 'Elastic', 'uiStateJSON': '{}', 'description': '', 'version': 1, 'kibanaSavedObjectMeta': {'searchSourceJSON': '{"query":{"query":"","language":"kuery"},"filter":[]}'}
#     },
#     'references': [{'name': 'metrics_0_index_pattern', 'type': 'index-pattern', 'id': '2e173190-af4c-11ec-a658-7fdb7f696a7c'}, {'name': 'metrics_1_index_pattern', 'type': 'index-pattern', 'id': '2e173190-af4c-11ec-a658-7fdb7f696a7c'}]
# }
#
#
#
#
# def create_timeseries_visualization(visualization_attributes):
#     CREATE_VIZUALIZATION_API = '/s/' + space_id + '/api/saved_objects/visualization/elastic2'
#     r = requests.post( KIBANA_URL + CREATE_VIZUALIZATION_API,
#                      auth=AUTH_DATA,
#                      headers=POST_HEADERS,
#                      json=visualization_attributes )
#     print(r.json())
#
# # create_timeseries_visualization(visualization_attributes)
#
# def get_visualization():
#     GET_VISUALIZATION_API = '/s/' + space_id + '/api/saved_objects/_find?type=lens'
#     r = requests.get(KIBANA_URL + GET_VISUALIZATION_API,
#                      auth=AUTH_DATA )
#     print(r.json()['saved_objects'][0])
# # get_dashboards()
# # get_visualization()
#
#
#
# def get_index_pattern():
#     GET_INDEX_PATTERN_API = '/s/' + space_id + '/api/saved_objects/_find?type=index_pattern'
#     r = requests.get(KIBANA_URL + GET_INDEX_PATTERN_API,
#                      auth=AUTH_DATA )
#     print(r.json())
# # get_index_pattern()
#
#
#
# lens_attributes = {
#  'attributes':
#  { 'title': 'test', 'description': '', 'visualizationType': 'lnsDatatable',
#    'state': {'visualization':
#     {'layerId': '639ebb2e-4a08-4597-bfa4-fa828ae636771', 'layerType': 'data',
#      'columns': [
#       {'columnId': '03215880-99f6-4823-b7d6-e5e910f4eec6', 'isTransposed': False,  'width': 191.16666666666663 },
#       {'columnId': '7ac194db-7e69-40a4-a21e-4033c2dbcd14', 'isTransposed': False  },
#       {'columnId': 'd7005def-41a9-45d5-ad65-4ec92b47adb8', 'isTransposed': False, 'alignment': 'left', 'width': 133.66666666666669},
#       {'columnId': 'ae5caa1f-6d6d-48e0-859d-eafeb2c66252', 'isTransposed': False, 'width': 265.3888888888889},
#       {'columnId': 'c7476644-309a-4a8f-a256-cd147843f3b2', 'isTransposed': False}]},
#       'query': {'query': '', 'language': 'kuery'},
#       'filters': [
#       {'meta': {'index': 'd706d6ca-48b2-49c1-8148-ce46e6b96d9c', 'alias': None, 'negate': False, 'disabled': False, 'type': 'phrase', 'key': 'level', 'params': {'query': 'error'}}, 'query': {'match_phrase': {'level': 'error'}}, '$state': {'store': 'appState'}}],
#       'datasourceStates':
#        {'indexpattern': {'layers': { '639ebb2e-4a08-4597-bfa4-fa828ae636771':
#         { 'columns':
#         {  '03215880-99f6-4823-b7d6-e5e910f4eec6': { 'label': 'time', 'dataType': 'date', 'operationType': 'date_histogram', 'sourceField': '@timestamp', 'isBucketed': True, 'scale': 'interval', 'params': {'interval': 'auto'}, 'customLabel': True},
#            '7ac194db-7e69-40a4-a21e-4033c2dbcd14': {'label': 'Count of records', 'dataType': 'number', 'operationType': 'count', 'isBucketed': False, 'scale': 'ratio', 'sourceField': '___records___'},
#            'd7005def-41a9-45d5-ad65-4ec92b47adb8': {'label': 'level', 'dataType': 'string', 'operationType': 'terms', 'scale': 'ordinal', 'sourceField': 'level.keyword', 'isBucketed': True, 'params': {'size': 3, 'orderBy': {'type': 'column', 'columnId': '7ac194db-7e69-40a4-a21e-4033c2dbcd14'},'orderDirection': 'desc', 'otherBucket': True, 'missingBucket': False, 'parentFormat': {'id': 'terms'}}, 'customLabel': True},
#            'ae5caa1f-6d6d-48e0-859d-eafeb2c66252': {'label': 'message', 'dataType': 'string', 'operationType': 'terms', 'scale': 'ordinal', 'sourceField': 'message.keyword', 'isBucketed': True, 'params': {'size': 3, 'orderBy': {'type': 'column', 'columnId': '7ac194db-7e69-40a4-a21e-4033c2dbcd14'}, 'orderDirection': 'desc', 'otherBucket': True, 'missingBucket': False, 'parentFormat': {'id': 'terms'}}, 'customLabel': True},
#            'c7476644-309a-4a8f-a256-cd147843f3b2': {'label': 'pod   name', 'dataType': 'string', 'operationType': 'terms', 'scale': 'ordinal', 'sourceField': 'kubernetes.pod_name.keyword', 'isBucketed': True, 'params': {'size': 3, 'orderBy': {'type': 'column', 'columnId': '7ac194db-7e69-40a4-a21e-4033c2dbcd14'}, 'orderDirection': 'desc', 'otherBucket': True, 'missingBucket': False, 'parentFormat': {'id': 'terms'}}, 'customLabel': True}},
#            'columnOrder': ['03215880-99f6-4823-b7d6-e5e910f4eec6', 'd7005def-41a9-45d5-ad65-4ec92b47adb8', 'ae5caa1f-6d6d-48e0-859d-eafeb2c66252', 'c7476644-309a-4a8f-a256-cd147843f3b2', '7ac194db-7e69-40a4-a21e-4033c2dbcd14'],
#             'incompleteColumns': {}}}}}}
#   },
#          'references': [
#           {'type': 'index-pattern', 'id': '24a204e0-affc-11ec-a658-7fdb7f696a7c', 'name': 'indexpattern-datasource-current-indexpattern'},
#           {'type': 'index-pattern', 'id': '24a204e0-affc-11ec-a658-7fdb7f696a7c', 'name': 'indexpattern-datasource-layer-639ebb2e-4a08-4597-bfa4-fa828ae636771'},
#           {'type': 'index-pattern', 'id': '24a204e0-affc-11ec-a658-7fdb7f696a7c', 'name': 'd706d6ca-48b2-49c1-8148-ce46e6b96d9c' }]
# }
#
# def create_lens_visualization(lens_attributes):
#     CREATE_LENS_API = '/s/' + space_id + '/api/saved_objects/lens/argocd'
#     r = requests.post( KIBANA_URL + CREATE_LENS_API,
#                      auth=AUTH_DATA,
#                      headers=POST_HEADERS,
#                      json=lens_attributes )
#     print(r.json())

# create_lens_visualization(lens_attributes)
kibanaSpaceManager = KibanaSpaceManager()
index_patterns = ('logstash-argocd-*','logstash-elastic-system-*','logstash-monitoring-*','logstash-cert-manager-*','logstash-kube-system-*','logstash-nginx-*')
space_name = 'devops'
kibanaSpaceManager.set_up_space(space_name,*index_patterns)
