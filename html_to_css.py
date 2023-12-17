def get_classes_from_html(html):
    classes = []
    i = 0

    while i < len(html):
        # Find the start of a tag
        start_tag = html.find("<", i)

        if start_tag == -1:
            break

        # Find the end of the tag
        end_tag = html.find(">", start_tag)

        if end_tag == -1:
            break

        # Extract the tag
        tag = html[start_tag:end_tag + 1]

        # Find the class attribute
        class_start = tag.find("class=")

        if class_start != -1:
            class_start += 6  # Move to the start of the class value

            # Find the start and end of the quotes surrounding the classes
            quote_start = tag[class_start]
            class_end = tag.find(quote_start, class_start + 1)

            if class_end != -1:
                classes.extend(tag[class_start + 1:class_end].split())

        # Move the index to the end of the processed tag
        i = end_tag + 1

    return classes


def generate_css_rules(classes):
    css_rules = ""
    for class_name in classes:
        css_rules += f".{class_name} {{}}\n"
    return css_rules


def main(html):
    classes = get_classes_from_html(html)
    css_rules = generate_css_rules(classes)
    return css_rules
