from PySide2.QtWidgets import QMessageBox, QDialog, QTableWidgetItem
from PySide2.QtCore import Qt


def display_message(title, message):
    """
    Displays a message with a title in a QMessageBox.
    :param title: Title of the message.
    :param message: Content of the message.
    """
    message_box = QMessageBox()
    message_box.setWindowTitle(title)
    message_box.setText(message)
    message_box.exec_()


def clear_issues_table(issues_table):
    while issues_table.rowCount() > 0:
        issues_table.removeRow(0)


def load_issues_table_data(table_widget, issues_dict):
    for index, issue_id in enumerate(issues_dict):
        table_widget.insertRow(index)
        issue_id_item = QTableWidgetItem(str(issue_id))
        issue_subject_item = QTableWidgetItem(str(issues_dict[issue_id]['subject']))
        issue_status_item = QTableWidgetItem(str(issues_dict[issue_id]['status']))
        issue_priority_item = QTableWidgetItem(str(issues_dict[issue_id]['priority']))
        issue_description_item = QTableWidgetItem(str(issues_dict[issue_id]['description']))
        issue_id_item.setTextAlignment(Qt.AlignHCenter)
        issue_subject_item.setTextAlignment(Qt.AlignHCenter)
        issue_status_item.setTextAlignment(Qt.AlignHCenter)
        issue_priority_item.setTextAlignment(Qt.AlignHCenter)
        issue_description_item.setTextAlignment(Qt.AlignHCenter)
        table_widget.setItem(index, 0, issue_id_item)
        table_widget.setItem(index, 1, issue_subject_item)
        table_widget.resizeColumnToContents(1)
        table_widget.setItem(index, 2, issue_status_item)
        table_widget.setItem(index, 3, issue_priority_item)
        table_widget.setItem(index, 4, issue_description_item)