"""
TODOC
"""


def x_to_table(items):
    """
    TODOC
    """
    table_json = []
    for i in items:
        row = {
            "Name":     i.name
        }
        table_json.append(row)
    return table_json


def admin_list_edit(items):
    """
    TODOC
    """
    table_json = []
    for i in items:
        row = {
            "Checkbox": "",
            "Name":     i.name,
            "Test":     "X"
        }
        table_json.append(row)
    return table_json


# def institutions_to_list_edit(items):
#     """
#     TODOC
#     """
#     table_json = []
#     for i in items:
#         row = {
#             "Name":     i.name
#         }
#         table_json.append(row)
#     return table_json


# def tags_to_list_edit(items):
#     """
#     TODOC
#     """
#     table_json = []
#     for i in items:
#         row = {
#             "Name":     i.name
#         }
#         table_json.append(row)
#     return table_json
