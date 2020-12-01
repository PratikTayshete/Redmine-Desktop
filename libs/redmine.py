from redminelib import Redmine


class RedMineManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__valid_redmine_login = None
        self.redmine = Redmine("http://127.0.0.1/redmine", username=self.username, password=self.password)

    def validate_login(self):
        is_user_valid = None
        try:
            if self.redmine.auth():
                self.__valid_redmine_login = True
                is_user_valid = True
        except Exception as error:
            print(error)
        return is_user_valid

    def get_projects(self):
        if self.__valid_redmine_login:
            projects_list = [project.name for project in self.redmine.project.all()]
            return projects_list
