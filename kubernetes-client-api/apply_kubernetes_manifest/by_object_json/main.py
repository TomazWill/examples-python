import yaml, json, tempfile, os
from kubernetes import client, config, utils


# My Object JSON
my_object_json = json.dumps(
    {
        "metadata": {
            "name": "my-test-pod"
        },
        "spec": {
            "containers": [
                {
                    "name": "test-container",
                    "image": "nginx",
                    "env": [
                        {
                            "name": "ENV",
                            "value": "dev"
                        }
                    ]
                }
            ]
        },
        "apiVersion": "v1",
        "kind": "Pod"
    }
)

# ------------------------------------------------------------

# Create new file with 'My Object JSON'(my_object_json)
fd, path_tmp_file = tempfile.mkstemp()
try:
    with os.fdopen(fd, 'w') as tmp:
        # create temp file with object Json (Kubernetes object)
        tmp.write(my_object_json)
        tmp.flush()
        print(f"\n\npath_tmp_file::: {path_tmp_file}")
finally:
    pass # For tests
    # os.remove(path_tmp_file)

# ------------------------------------------------------------

print(f"\n\njson.dumps::: {my_object_json}")
print(f"\n\nyaml.dump::: {yaml.dump(my_object_json)}")

# ------------------------------------------------------------

# Load kube_config
config.load_kube_config()
# Get ApiClient (with defult configuration)
k8s_client = client.ApiClient()

# Apply file in Kubernetes 
utils.create_from_yaml(k8s_client, path_tmp_file)

# Delete tmp_file after apply on Kubernetes
os.remove(path_tmp_file)