import requests
import os

POST_HEADERS = {'Content-Type':'application/json', 'kbn-xsrf' : 'true'}

class KibanaSpaceManager(object):
    """docstring for ."""

    def __init__(self):
        self.KIBANA_URL = os.environ['KIBANA_URL']
        self.KIBANA_USER = os.environ['KIBANA_USER']
        self.KIBANA_PASSWORD = os.environ['KIBANA_PASSWORD']
        self.AUTH_DATA = ( self.KIBANA_USER, self.KIBANA_PASSWORD )

    def set_up_space(self, space_name, *index_patterns):

        space_id = self.create_space(space_name)
        for index_pattern in index_patterns:
            panel_json_arr = []
            index_pattern_id = self.create_index_pattern(index_pattern,space_id)
            lens_id = self.create_lens_visualization(space_id, index_pattern ,index_pattern_id)
            # panel_json_arr = self.insert_lens_id_to_panel(lens_id, panel_json_arr)
            vis_timeseries_id = self.create_timeseries_visualization(space_id, index_pattern ,index_pattern_id)
            panel_json_arr = self.insert_vis_id_to_panel(vis_timeseries_id,panel_json_arr)
            vis_metric_id = self.create_metric_visualization(space_id, index_pattern ,index_pattern_id)
            panel_json_arr = self.insert_vis_id_to_panel(vis_metric_id,panel_json_arr)
            self.create_dashboard(space_id, index_pattern, panel_json_arr)

    def create_space(self,space_name):
        space_attributes = {
            "id": space_name,
            "name": space_name
        }
        CREATE_SPACE_API = '/api/spaces/space'
        space_response = requests.post( self.KIBANA_URL + CREATE_SPACE_API,
                                     auth=self.AUTH_DATA,
                                     headers=POST_HEADERS,
                                     json=space_attributes)

        if space_response.status_code != 200:
            raise Exception(space_response.text)
        else:
            print('Space ' + space_name + ' has been created')
            return space_response.json()['id']


    def create_index_pattern(self, index_pattern, space_id):
        index_pattern_attributes = {
            "index_pattern" : { "title": index_pattern }
        }
        CREATE_INDEX_PATTERN_API = '/s/' + space_id + '/api/index_patterns/index_pattern'
        index_pattern_response = requests.post( self.KIBANA_URL + CREATE_INDEX_PATTERN_API,
                        auth=self.AUTH_DATA ,
                        headers=POST_HEADERS,
                        json=index_pattern_attributes)


        if index_pattern_response.status_code != 200:
            raise Exception(index_pattern_response.text)
        else:
            print('Index pattern ' + index_pattern + ' has been created')
            return index_pattern_response.json()['index_pattern']['id']


    def create_timeseries_visualization(self,space_id, index_pattern, index_pattern_id):
        title = index_pattern.replace("-*", "")
        vis_state = '{"title":"{title_param}","type":"metrics","aggs":[],"params":{"time_range_mode":"entire_time_range","id":"2f1f7bed-7a0f-4f1f-9d7c-9e26aa401cf9","type":"timeseries","series":[{"time_range_mode":"entire_time_range","id":"771795ae-89b9-4f52-9f06-5a93941efd5b","color":"#68BC00","split_mode":"terms","palette":{"type":"palette","name":"default"},"metrics":[{"id":"364769d4-8ec6-4d77-82a8-               03068c5c9d99","type":"count"}],"separate_axis":0,"axis_position":"right","formatter":"default","chart_type":"line","line_width":1,"point_size":1,"fill":0.5,"stacked":"none","override_index_pattern":0,"series_drop_last_bucket":0,"terms_field":"level.keyword"}],"time_field":"@timestamp","use_kibana_indexes":true,"interval":"","axis_position":"left","axis_formatter":"number","axis_scale":"normal","show_legend":1,"truncate_legend":1,"max_lines_legend":1,"show_grid":1,"tooltip_mode":"show_all","drop_last_bucket":0,"isModelInvalid":false,"index_pattern_ref_name":"metrics_0_index_pattern"}}'.replace('{title_param}', title)
        visualization_attributes = {
            'attributes': {
            'visState': vis_state,
             'title': title + '-timeseries',
             'uiStateJSON': '{}',
             'description': '',
             'version': 1,
             'kibanaSavedObjectMeta': {'searchSourceJSON': '{"query":{"query":"","language":"kuery"},"filter":[]}'
            }},
             'references': [{'name': 'metrics_0_index_pattern', 'type': 'index-pattern', 'id': index_pattern_id}]
        }

        CREATE_VIZUALIZATION_API = '/s/' + space_id + '/api/saved_objects/visualization/' + title + '-timeseries'
        vis_response = requests.post( self.KIBANA_URL + CREATE_VIZUALIZATION_API,
                         auth=self.AUTH_DATA,
                         headers=POST_HEADERS,
                         json=visualization_attributes )
        if vis_response.status_code != 200:
            raise Exception(vis_response.text)
        else:
            print('Visualization timeseries ' + title + ' has been created')
            return vis_response.json()['id']

    def create_lens_visualization(self,space_id, index_pattern, index_pattern_id):
        title = index_pattern.replace("-*","")
        title = title + '-table'
        lens_attributes = {
         'attributes':
         { 'title': title, 'description': '', 'visualizationType': 'lnsDatatable',
           'state': {'visualization':
            {'layerId': '639ebb2e-4a08-4597-bfa4-fa828ae636771', 'layerType': 'data',
             'columns': [
              {'columnId': '03215880-99f6-4823-b7d6-e5e910f4eec6', 'isTransposed': False,  'width': 191.16666666666663 },
              {'columnId': '7ac194db-7e69-40a4-a21e-4033c2dbcd14', 'isTransposed': False  },
              {'columnId': 'd7005def-41a9-45d5-ad65-4ec92b47adb8', 'isTransposed': False, 'alignment': 'left', 'width': 133.66666666666669},
              {'columnId': 'ae5caa1f-6d6d-48e0-859d-eafeb2c66252', 'isTransposed': False, 'width': 265.3888888888889},
              {'columnId': 'c7476644-309a-4a8f-a256-cd147843f3b2', 'isTransposed': False}]},
              'query': {'query': '', 'language': 'kuery'},
              'filters': [
              {'meta': {'index': 'd706d6ca-48b2-49c1-8148-ce46e6b96d9c', 'alias': None, 'negate': False, 'disabled': False, 'type': 'phrase', 'key': 'level', 'params': {'query': 'error'}}, 'query': {'match_phrase': {'level': 'error'}}, '$state': {'store': 'appState'}}],
              'datasourceStates':
               {'indexpattern': {'layers': { '639ebb2e-4a08-4597-bfa4-fa828ae636771':
                { 'columns':
                {  '03215880-99f6-4823-b7d6-e5e910f4eec6': { 'label': 'time', 'dataType': 'date', 'operationType': 'date_histogram', 'sourceField': '@timestamp', 'isBucketed': True, 'scale': 'interval', 'params': {'interval': 'auto'}, 'customLabel': True},
                   '7ac194db-7e69-40a4-a21e-4033c2dbcd14': {'label': 'Count of records', 'dataType': 'number', 'operationType': 'count', 'isBucketed': False, 'scale': 'ratio', 'sourceField': '___records___'},
                   'd7005def-41a9-45d5-ad65-4ec92b47adb8': {'label': 'level', 'dataType': 'string', 'operationType': 'terms', 'scale': 'ordinal', 'sourceField': 'level.keyword', 'isBucketed': True, 'params': {'size': 3, 'orderBy': {'type': 'column', 'columnId': '7ac194db-7e69-40a4-a21e-4033c2dbcd14'},'orderDirection': 'desc', 'otherBucket': True, 'missingBucket': False, 'parentFormat': {'id': 'terms'}}, 'customLabel': True},
                   'ae5caa1f-6d6d-48e0-859d-eafeb2c66252': {'label': 'message', 'dataType': 'string', 'operationType': 'terms', 'scale': 'ordinal', 'sourceField': 'message.keyword', 'isBucketed': True, 'params': {'size': 3, 'orderBy': {'type': 'column', 'columnId': '7ac194db-7e69-40a4-a21e-4033c2dbcd14'}, 'orderDirection': 'desc', 'otherBucket': True, 'missingBucket': False, 'parentFormat': {'id': 'terms'}}, 'customLabel': True},
                   'c7476644-309a-4a8f-a256-cd147843f3b2': {'label': 'pod   name', 'dataType': 'string', 'operationType': 'terms', 'scale': 'ordinal', 'sourceField': 'kubernetes.pod_name.keyword', 'isBucketed': True, 'params': {'size': 3, 'orderBy': {'type': 'column', 'columnId': '7ac194db-7e69-40a4-a21e-4033c2dbcd14'}, 'orderDirection': 'desc', 'otherBucket': True, 'missingBucket': False, 'parentFormat': {'id': 'terms'}}, 'customLabel': True}},
                   'columnOrder': ['03215880-99f6-4823-b7d6-e5e910f4eec6', 'd7005def-41a9-45d5-ad65-4ec92b47adb8', 'ae5caa1f-6d6d-48e0-859d-eafeb2c66252', 'c7476644-309a-4a8f-a256-cd147843f3b2', '7ac194db-7e69-40a4-a21e-4033c2dbcd14'],
                    'incompleteColumns': {}}}}}}
          },
                 'references': [
                  {'type': 'index-pattern', 'id': index_pattern_id, 'name': 'indexpattern-datasource-current-indexpattern'},
                  {'type': 'index-pattern', 'id': index_pattern_id, 'name': 'indexpattern-datasource-layer-639ebb2e-4a08-4597-bfa4-fa828ae636771'},
                  {'type': 'index-pattern', 'id': index_pattern_id, 'name': 'd706d6ca-48b2-49c1-8148-ce46e6b96d9c' }]
        }
        CREATE_LENS_API = '/s/' + space_id + '/api/saved_objects/lens/' + title
        lens_response = requests.post( self.KIBANA_URL + CREATE_LENS_API,
                             auth=self.AUTH_DATA,
                             headers=POST_HEADERS,
                             json=lens_attributes )
        if lens_response.status_code != 200:
            raise Exception(lens_response.text)
        else:
            print('Lens ' + title + ' has been created')
            return lens_response.json()['id']
    def create_metric_visualization(self,space_id, index_pattern, index_pattern_id):
        title = index_pattern.replace("-*", "")
        vis_state = '{"title":"{title_param}","type":"metrics","aggs":[],"params":{"time_range_mode":"entire_time_range","id":"2f1f7bed-7a0f-4f1f-9d7c-9e26aa401cf9","type":"metric","series":[{"time_range_mode":"entire_time_range","id":"771795ae-89b9-4f52-9f06-5a93941efd5b","color":"#68BC00","split_mode":"terms","palette":{"type":"palette","name":"default"},"metrics":[{"id":"364769d4-8ec6-4d77-82a8-               03068c5c9d99","type":"count"}],"separate_axis":0,"axis_position":"right","formatter":"default","chart_type":"line","line_width":1,"point_size":1,"fill":0.5,"stacked":"none","override_index_pattern":0,"series_drop_last_bucket":0,"terms_field":"level.keyword"}],"time_field":"@timestamp","use_kibana_indexes":true,"interval":"","axis_position":"left","axis_formatter":"number","axis_scale":"normal","show_legend":1,"truncate_legend":1,"max_lines_legend":1,"show_grid":1,"tooltip_mode":"show_all","drop_last_bucket":0,"isModelInvalid":false,"index_pattern_ref_name":"metrics_0_index_pattern"}}'.replace('{title_param}', title)
        visualization_attributes = {
            'attributes': {
            'visState': vis_state,
             'title': title + '-metric',
             'uiStateJSON': '{}',
             'description': '',
             'version': 1,
             'kibanaSavedObjectMeta': {'searchSourceJSON': '{"query":{"query":"","language":"kuery"},"filter":[]}'
            }},
             'references': [{'name': 'metrics_0_index_pattern', 'type': 'index-pattern', 'id': index_pattern_id}]
        }

        CREATE_VIZUALIZATION_API = '/s/' + space_id + '/api/saved_objects/visualization/' + title + '-metric'
        vis_response = requests.post( self.KIBANA_URL + CREATE_VIZUALIZATION_API,
                         auth=self.AUTH_DATA,
                         headers=POST_HEADERS,
                         json=visualization_attributes )
        if vis_response.status_code != 200:
            raise Exception(vis_response.text)
        else:
            print('Visualization metric ' + title + ' has been created')
            return vis_response.json()['id']




    def create_dashboard(self, space_id, index_pattern, panel_json_arr):
        title = index_pattern.replace("-*", "")
        panel_json = '[' + ','.join(panel_json_arr) + ']'
        dashboard_attributes = {
            "attributes" :
        {
             'title': title,
             'hits': 0,
             'description': title,
             'panelsJSON': panel_json,
             'optionsJSON': '{"useMargins":true,"syncColors":false,"hidePanelTitles":false}',
             'version': 1,
             'timeRestore': False,
             'kibanaSavedObjectMeta': {'searchSourceJSON': '{"query":{"query":"","language":"kuery"},"filter":[]}'}}
        }
        CREATE_DASHBOARD_API = '/s/' + space_id + '/api/saved_objects/dashboard/' + title
        dashboard_response = requests.post( self.KIBANA_URL + CREATE_DASHBOARD_API,
                         auth=self.AUTH_DATA,
                         headers=POST_HEADERS,
                         json=dashboard_attributes )
        if dashboard_response.status_code != 200:
            raise Exception(dashboard_response.text)
        else:
            print('Dashboard ' + title + ' has been created')


    def insert_vis_id_to_panel(self,vis_id,panel_json_arr):
        panel_template = '{"gridData":{"w":100,"h":15,"x":0,"y":0,"i":"{index}"},"version":"7.0.0-alpha1","panelIndex":"{index}","type":"visualization","id":"{index}","embeddableConfig":{}}'
        panel_element = panel_template.replace('{index}', vis_id)
        panel_json_arr.append(panel_element)
        return panel_json_arr

    def insert_lens_id_to_panel(self,lens_id,panel_json_arr):
        panel_template = '{"gridData":{"w":100,"h":15,"x":0,"y":0,"i":"{index}"},"version":"7.0.0-alpha1","panelIndex":"{index}","type":"lens","id":"{index}","embeddableConfig":}'
        panel_element = panel_template.replace('{index}', lens_id)
        panel_json_arr.append(panel_element)
        return panel_json_arr
