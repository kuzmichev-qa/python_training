from sys import maxsize

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="group_name_1", header="group_header_1", footer="group_footer_1")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize

    assert sorted(old_groups, key=id_or_max) == sorted(new_groups, key=id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
