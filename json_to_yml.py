import json
import yaml


def convert_json_to_yaml(json_input):
    try:
        data = json.loads(json_input)

        yaml_output = yaml.dump(data, default_flow_style=False, sort_keys=False)

        return yaml_output
    except Exception as e:
        return f"Error: {str(e)}"
