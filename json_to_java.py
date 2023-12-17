def generate_java_class(json_input):
    java_class = f"public class Main {{\n"
    for key, value in json_input.items():
        if isinstance(value, list):
            java_class += f"    private List<{key.capitalize()}> {key};\n"
        else:
            java_class += f"    private {type_to_java(value)} {key};\n"
    for key, value in json_input.items():
        if isinstance(value, list):
            java_class += f"    public static class {key.capitalize()} {{\n"
            for sub_key, sub_value in value[0].items():
                java_class += f"        private {type_to_java(sub_value)} {sub_key};\n"
            java_class += "    }\n"
    java_class += "}\n"
    return java_class


def type_to_java(value):
    if isinstance(value, bool):
        return "boolean"
    elif isinstance(value, int):
        return "int"
    elif isinstance(value, float):
        return "double"
    elif isinstance(value, list):
        return "List<String>"
    else:
        return "String"
