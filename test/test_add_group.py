from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="group_name_1", header="group_header_1", footer="group_footer_1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
