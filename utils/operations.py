from PySide2.QtWidgets import QMessageBox


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
