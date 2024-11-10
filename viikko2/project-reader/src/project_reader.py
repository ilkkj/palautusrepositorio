from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_toml = toml.loads(content)

        name = parsed_toml.get("tool", {}).get("poetry", {}).get("name")
        description = parsed_toml.get("tool", {}).get("poetry", {}).get("description")
        license = parsed_toml.get("tool", {}).get("poetry", {}).get("license")
        authors = parsed_toml.get("tool", {}).get("poetry", {}).get("authors", [])
        dependencies = list(parsed_toml.get("tool", {}).get("poetry", {}).get("dependencies", {}).keys())
        dev_dependencies = list(parsed_toml.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", {}).keys())

        return Project(name, description, license, authors, dependencies, dev_dependencies)
