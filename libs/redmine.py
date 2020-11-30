from redminelib import Redmine


class RedMineManager:
    def __init__(self, username, password):
        self.username = username
        self.__valid_redmine_login = False
        self.__validate_login(self.username, password)

    def __validate_login(self, username, password):
        try:
            self.redmine = Redmine("http://127.0.0.1/redmine", username=username, password=password)
            if self.redmine.auth():
                self.__valid_redmine_login = True
        except Exception as error:
            print(error)

    def get_projects(self):
        if self.__valid_redmine_login:
            projects_list = [project.name for project in self.redmine.project.all()]
            return projects_list
