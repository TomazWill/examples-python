from kubernetes import client, config, utils

config.load_kube_config()

k8s_client = client.ApiClient()
yaml_file = 'apply_files_k8s/meu-pod.yml'
utils.create_from_yaml(k8s_client, yaml_file)