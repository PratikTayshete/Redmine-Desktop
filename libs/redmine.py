from redminelib import Redmine
from utils import constants


class RedMineManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__valid_redmine_login = None
        self.projects_list = None
        self.issues_dict = None
        self.redmine = Redmine("http://127.0.0.1/redmine", username=self.username, password=self.password)

    def validate_login(self):
        """
        Validates the login credentials of the user.
        """
        is_user_valid = None
        try:
            if self.redmine.auth():
                self.__valid_redmine_login = True
                is_user_valid = True
        except Exception as error:
            print(error)
        return is_user_valid

    def get_projects(self):
        """
        Gets the list of projects.
        :return: projects_list: A list of names of all the projects.
        """
        if self.__valid_redmine_login:
            self.projects_list = [project.name for project in self.redmine.project.all()]
            projects_list = self.projects_list
            return projects_list

    def total_projects_count(self):
        """
        Gets the total number of projects.
        :return: total_projects: A total count of all the projects.
        """
        total_projects = str(len(self.get_projects()))
        return total_projects

    def get_issues(self):
        """
        Gets all the issues created by the user.
        :return: issues_dict: A dictionary that contains issues created by the user along with some of its information.
        """
        if self.__valid_redmine_login:
            self.issues_dict = {}
            for issue in self.redmine.issue.all():
                issue_dict = {'subject': issue.subject,
                              'status': str(issue.status),
                              'priority': str(issue.priority),
                              'description': issue.description
                              }
                self.issues_dict[issue.id] = issue_dict
        issues_dict = self.issues_dict
        return issues_dict

    def total_issues_count(self):
        """
        Gets the total number of issues created by the user.
        :return: total_issues: A total count of all the issues.
        """
        if self.__valid_redmine_login:
            total_issues = str(len(self.get_issues()))
            return total_issues

    def total_issues_resolved_count(self):
        """
        Gets the total number of issues whose status is resolved.
        :return: total_resolved: A total count of issues whose status is resolved.
        """
        if self.__valid_redmine_login:
            total_resolved = 0
            for issue_key in self.issues_dict:
                if self.issues_dict[issue_key]['status'] == constants.RESOLVED_STATUS:
                    total_resolved += 1
            total_resolved = str(total_resolved)
            return total_resolved

    def total_issues_pending_count(self):
        """
        Gets the total number of issues whose status is not resolved.
        :return: total_pending: A total count of issues whose status is not resolved.
        """
        if self.__valid_redmine_login:
            total_pending = 0
            for issue_key in self.issues_dict:
                if self.issues_dict[issue_key]['status'] != constants.RESOLVED_STATUS:
                    total_pending += 1
            total_pending = str(total_pending)
            return total_pending

    def clear_data_on_logout(self):
        """
        Reassigns variables to None.
        """
        self.projects_list = None
        self.issues_dict = None
        self.redmine = None
        self.__valid_redmine_login = None
