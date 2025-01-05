from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ComponentView(LoginRequiredMixin,TemplateView):
    pass


# Base Ui
accordions_view = ComponentView.as_view(
    template_name="components/base-ui/accordions.html"
)
alerts_view = ComponentView.as_view(template_name="components/base-ui/alerts.html")
avatars_view = ComponentView.as_view(template_name="components/base-ui/avatars.html")
badges_view = ComponentView.as_view(template_name="components/base-ui/badges.html")
breadcrumb_view = ComponentView.as_view(
    template_name="components/base-ui/breadcrumb.html"
)
buttons_view = ComponentView.as_view(template_name="components/base-ui/buttons.html")
cards_view = ComponentView.as_view(template_name="components/base-ui/cards.html")
carousel_view = ComponentView.as_view(template_name="components/base-ui/carousel.html")
collapse_view = ComponentView.as_view(template_name="components/base-ui/collapse.html")
dropdowns_view = ComponentView.as_view(
    template_name="components/base-ui/dropdowns.html"
)
embed_video_view = ComponentView.as_view(
    template_name="components/base-ui/embed-video.html"
)
grid_view = ComponentView.as_view(template_name="components/base-ui/grid.html")
links_view = ComponentView.as_view(template_name="components/base-ui/links.html")
list_group_view = ComponentView.as_view(
    template_name="components/base-ui/list-group.html"
)
modals_view = ComponentView.as_view(template_name="components/base-ui/modals.html")
notifications_view = ComponentView.as_view(
    template_name="components/base-ui/notifications.html"
)
offcanvas_view = ComponentView.as_view(
    template_name="components/base-ui/offcanvas.html"
)
placeholders_view = ComponentView.as_view(
    template_name="components/base-ui/placeholders.html"
)
pagination_view = ComponentView.as_view(
    template_name="components/base-ui/pagination.html"
)
popovers_view = ComponentView.as_view(template_name="components/base-ui/popovers.html")
progress_view = ComponentView.as_view(template_name="components/base-ui/progress.html")
spinners_view = ComponentView.as_view(template_name="components/base-ui/spinners.html")
tabs_view = ComponentView.as_view(template_name="components/base-ui/tabs.html")
tooltips_view = ComponentView.as_view(template_name="components/base-ui/tooltips.html")
typography_view = ComponentView.as_view(
    template_name="components/base-ui/typography.html"
)
utilities_view = ComponentView.as_view(
    template_name="components/base-ui/utilities.html"
)

# Extended Ui
extended_dragula_view = ComponentView.as_view(
    template_name="components/extended-ui/extended-dragula.html"
)
extended_range_slider_view = ComponentView.as_view(
    template_name="components/extended-ui/extended-range-slider.html"
)
extended_ratings_view = ComponentView.as_view(
    template_name="components/extended-ui/extended-ratings.html"
)
extended_scrollbar_view = ComponentView.as_view(
    template_name="components/extended-ui/extended-scrollbar.html"
)
extended_scrollspy_view = ComponentView.as_view(
    template_name="components/extended-ui/extended-scrollspy.html"
)

# Widgets
widgets_view = ComponentView.as_view(template_name="components/widgets/widgets.html")

# Icons
icons_remixicons_view = ComponentView.as_view(
    template_name="components/icons/icons-remixicons.html"
)
icons_bootstrap_view = ComponentView.as_view(
    template_name="components/icons/icons-bootstrap.html"
)
icons_material_view = ComponentView.as_view(
    template_name="components/icons/icons-material-symbol.html"
)

# Charts
# Apex
apex_area_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-area.html"
)
apex_bar_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-bar.html"
)
apex_bubble_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-bubble.html"
)
apex_candlestick_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-candlestick.html"
)
apex_column_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-column.html"
)
apex_heatmap_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-heatmap.html"
)
apex_line_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-line.html"
)
apex_mixed_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-mixed.html"
)
apex_timeline_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-timeline.html"
)
apex_boxplot_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-boxplot.html"
)
apex_treemap_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-treemap.html"
)
apex_pie_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-pie.html"
)
apex_radar_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-radar.html"
)
apex_radialbar_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-radialbar.html"
)
apex_scatter_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-scatter.html"
)
apex_polar_area_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-polar-area.html"
)
apex_sparklines_view = ComponentView.as_view(
    template_name="components/charts/apex-charts/apex-sparklines.html"
)
# ChartJs
chartjs_area_view = ComponentView.as_view(
    template_name="components/charts/chartjs/chartjs-area.html"
)
chartjs_bar_view = ComponentView.as_view(
    template_name="components/charts/chartjs/chartjs-bar.html"
)
chartjs_line_view = ComponentView.as_view(
    template_name="components/charts/chartjs/chartjs-line.html"
)
chartjs_other_view = ComponentView.as_view(
    template_name="components/charts/chartjs/chartjs-other.html"
)


# Forms
form_elements_view = ComponentView.as_view(
    template_name="components/forms/form-elements.html"
)
form_advanced_view = ComponentView.as_view(
    template_name="components/forms/form-advanced.html"
)
form_validation_view = ComponentView.as_view(
    template_name="components/forms/form-validation.html"
)
form_wizard_view = ComponentView.as_view(
    template_name="components/forms/form-wizard.html"
)
form_fileuploads_view = ComponentView.as_view(
    template_name="components/forms/form-fileuploads.html"
)
form_editors_view = ComponentView.as_view(
    template_name="components/forms/form-editors.html"
)


# Tables
tables_basic_view = ComponentView.as_view(
    template_name="components/tables/tables-basic.html"
)
tables_datatable_view = ComponentView.as_view(
    template_name="components/tables/tables-datatable.html"
)


# Maps
google_map_view = ComponentView.as_view(
    template_name="components/maps/maps-google.html"
)
vector_map_view = ComponentView.as_view(
    template_name="components/maps/maps-vector.html"
)
