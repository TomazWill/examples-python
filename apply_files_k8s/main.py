from kubernetes import client, config, utils

config.load_kube_config()

k8s_client = client.ApiClient()

# APLICANDO COM ARQUIVO YML
yaml_file = 'apply_files_k8s/meu-pod.meu-pod.yml'
utils.create_from_yaml(k8s_client, yaml_file)

# APLICANDO COM ARQUIVO JSON
json_file = 'apply_files_k8s/meu-pod.json'
utils.create_from_yaml(k8s_client, json_file)
