from utils.menus import ViewMenuItem

from menu import Menu, MenuItem

from django.core.urlresolvers import reverse

# Since we use ViewMenuItem here we do not need to define checks, instead
# the check logic will change their visibility based on the permissions
# attached to the views we reverse here.
reports_children = (
     ViewMenuItem("Staff Only", reverse("reports.views.staff")),
     ViewMenuItem("Superuser Only", reverse("reports.views.superuser"))
)

Menu.add_item("main", MenuItem("Reports Index",
                               reverse("reports.views.index"),
                               children=reports_children))