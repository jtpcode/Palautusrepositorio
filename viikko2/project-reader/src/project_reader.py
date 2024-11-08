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
        des = toml.loads(content)
        return Project(des['tool']['poetry']['name'], des['tool']['poetry']['description'], des['tool']['poetry']['license'],
                       des['tool']['poetry']['authors'], list(des['tool']['poetry']['dependencies'].keys()),
                       list(des['tool']['poetry']['group']['dev']['dependencies'].keys()))
