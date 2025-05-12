"""
TODOC
"""

from flask_app.data_models import Account

# region Classes
class ListSettings:
    """
    TODOC
    """
    def __init__(self, items):
        self.id         = None
        self.wide       = "3"
        self.items      = items

class ListItem:
    """
    TODOC
    Recognizes the following attributes from properties:
        - label
        - link
        - color
        - disabled
    """
    def __init__(self, properties):
        for key, value in properties.items():
            setattr(self, key, value)


class Table:
    """
    TODOC
    """
    def __init__(self, **properties):
        self.id             = None
        self.entity         = None
        self.type           = "list_edit"
        self.columns        = None
        # self.data           = None

        for key, value in properties.items():
            setattr(self, key, value)

        # self.define_row_data()
        self.define_columns()

    # def define_row_data(self, data):
        # """
        # TODOC
        # """
        # if self.type is "list_edit":
        # self.data = [item.to_list_edit() for item in data]

    def define_columns(self):
        """
        TODOC
        """
        # if self.type == "list_edit":
        #     if isinstance(data[0], Account):
        # HACK
        self.columns = ['Name', 'Type', 'Institution']


# class TableColumn:
#     """
#     TODOC
#     """
#     def __init__(self, **properties):
#         self.properties         = None
#         self.field              = None
#         self.title              = None
#         self.data_field         = None
#         self.data_checkbox      = None

#         for key, value in properties.items():
#             setattr(self, key, value)

#         self.set_properties()

#     def set_properties(self):
#         """
#         TODOC
#         """
#         # for key in vars(self):
#         #     yield key
#         self.properties = list(vars(self))


# class TableRow:
#     """
#     TODOC
#     """
#     def __init__(self, data):
#         self.field = data.field
#         self.title = data.title
#         self.event = data.event
# endregion Classes


# region List Definitions
def admin_index_list(**properties):
    """
    TODOC
    """
    admin_index_items = [
        {
            "label":    "Institutions",
            "link":     "admin/institutions",
            "color":    "info"
        },
        {
            "label":    "Accounts",
            "link":     "admin/accounts",
            "color":    "info"
        },
        {
            "label":    "Payees",
            "link":     "admin/payees",
            "color":    "info",
            "disabled": True
        },
        {
            "label":    "Spending Categories",
            "link":     "admin/categories",
            "color":    "info",
            "disabled": True
        },
        {
            "label":    "Tags",
            "link":     "admin/tags",
            "color":    "info",
        },
        {
            "label":    "App Settings",
            "link":     "admin/settings",
            "color":    "info",
            "disabled": True
        },
        {
            "label":    "User Preferences",
            "link":     "admin/prefs",
            "disabled": True
        }
    ]
    items = []
    for item in admin_index_items:
        items.append(ListItem(item))
    settings = ListSettings(items)
    for key, value in properties.items():
        setattr(settings, key, value)
    return settings
# endregion Definitions
