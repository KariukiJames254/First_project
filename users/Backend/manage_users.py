from base.Backend.services import TeacherService


class ManageUsers(object):
    teachers = TeacherService().filter()

