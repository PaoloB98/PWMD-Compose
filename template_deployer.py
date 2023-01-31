from jinja2 import Environment, FileSystemLoader, select_autoescape, Template

# importing the module
import json


def template_deploy(template_file_name: str, result_file_name: str, ):
    # reading the data from the file
    with open('./config_templates/dictionary.json') as f:
        data = f.read()
    f.close()

    dict = json.loads(data)

    env = Environment(
        loader=FileSystemLoader("./config_templates"),
        autoescape=select_autoescape()
    )
    t = env.get_template(template_file_name)

    render = t.render(dict)

    config_file = open(result_file_name, "w")
    config_file.write(render)
    config_file.close()

    print("DONE")


if __name__ == '__main__':
    template_deploy("docker-compose-template.jinja", "docker-compose.yaml")
    template_deploy("nginx-template.jinja", "nginx/nginx.conf")
    template_deploy("postfix-config-template.jinja", "postfix/main.cf")
    template_deploy("virtusertable-template.jinja", "postfix/virtusertable")
