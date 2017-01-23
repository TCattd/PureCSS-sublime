#esteban@attitude.cl
import sublime, sublime_plugin

#Base
purecss_classes = ["pure-img"]

#Grids
purecss_classes.extend(["pure-g", "pure-u-", "pure-u-sm-", "pure-u-md-", "pure-u-lg-", "pure-u-xl-"])

#Form
purecss_classes.extend(["pure-form", "pure-form-stacked", "pure-form-aligned", "pure-group", "pure-input-", "pure-input-rounded", "pure-checkbox", "pure-radio"])

#Buttons
purecss_classes.extend(["pure-button", "pure-button-disabled", "pure-button-active", "pure-button-primary", "pure-button-group"])

#Tables
purecss_classes.extend(["pure-table", "pure-table-bordered", "pure-table-horizontal", "pure-table-odd", "pure-table-striped"])

#Menus
purecss_classes.extend(["pure-menu", "pure-menu-horizontal", "pure-menu-selected", "pure-menu-heading", "pure-menu-open", "pure-menu-separator", "pure-menu-disabled", "pure-paginator"])

#Custom. Please Ref: https://github.com/yui/pure/issues/326
purecss_classes.extend(["pure-hidden-sd", "pure-hidden-md", "pure-hidden-lg", "pure-hidden-xl"])

#Hidden in PX
'''
/* pure-hidden-xs */
@media screen and (max-width:567px) {
    .pure-visible-sm{display:none}
    .pure-visible-md{display:none}
    .pure-visible-lg{display:none}
    .pure-visible-xl{display:none}
    .pure-hidden-xs{display:none}
}
/* pure-hidden-sm */
@media screen and (min-width:568px) and (max-width:767px) {
    .pure-visible-xs{display:none}
    .pure-visible-md{display:none}
    .pure-visible-lg{display:none}
    .pure-visible-xl{display:none}
    .pure-hidden-sm{display:none}
}
/* pure-hidden-md */
@media screen and (min-width:768px) and (max-width:1023px) {
    .pure-visible-xs{display:none}
    .pure-visible-sm{display:none}
    .pure-visible-lg{display:none}
    .pure-visible-xl{display:none}
    .pure-hidden-md{display:none}
}
/* pure-hidden-lg */
@media screen and (min-width:1024px) and (max-width:1279px) {
    .pure-visible-xs{display:none}
    .pure-visible-sm{display:none}
    .pure-visible-md{display:none}
    .pure-visible-xl{display:none}
    .pure-hidden-lg{display:none}
}
/* pure-hidden-xl */
@media screen and (min-width:1280px) {
    .pure-visible-xs{display:none}
    .pure-visible-sm{display:none}
    .pure-visible-md{display:none}
    .pure-visible-lg{display:none}
    .pure-hidden-xl{display:none}
}
'''

#Hidden in EM
'''
/* pure-hidden-xs */
@media screen and (max-width:35.438em) {
    .pure-visible-sm{display:none}
    .pure-visible-md{display:none}
    .pure-visible-lg{display:none}
    .pure-visible-xl{display:none}
    .pure-hidden-xs{display:none}
}
/* pure-hidden-sm */
@media screen and (min-width:35.5em) and (max-width:47.938em) {
    .pure-visible-xs{display:none}
    .pure-visible-md{display:none}
    .pure-visible-lg{display:none}
    .pure-visible-xl{display:none}
    .pure-hidden-sm{display:none}
}
/* pure-hidden-md */
@media screen and (min-width:48em) and (max-width:63.938em) {
    .pure-visible-xs{display:none}
    .pure-visible-sm{display:none}
    .pure-visible-lg{display:none}
    .pure-visible-xl{display:none}
    .pure-hidden-md{display:none}
}
/* pure-hidden-lg */
@media screen and (min-width:64em) and (max-width:79.938em) {
    .pure-visible-xs{display:none}
    .pure-visible-sm{display:none}
    .pure-visible-md{display:none}
    .pure-visible-xl{display:none}
    .pure-hidden-lg{display:none}
}
/* pure-hidden-xl */
@media screen and (min-width:80em) {
    .pure-visible-xs{display:none}
    .pure-visible-sm{display:none}
    .pure-visible-md{display:none}
    .pure-visible-lg{display:none}
    .pure-hidden-xl{display:none}
}
'''

#Attr
purecss_attr = ["hidden", "required", "disabled", "readonly"]

class PureCSSCompletions(sublime_plugin.EventListener):
    def __init__(self):
        self.class_completions = [("%s \tPureCSS class" % s, s) for s in purecss_classes]
        self.attr_completions = [("%s \tPureCSS attr" % s, s) for s in purecss_attr]

    def on_query_completions(self, view, prefix, locations):
        #Thanks to https://github.com/uikit/uikit-sublime for this snippet. All credits to YOOtheme GmbH (MIT licenced)
        if view.match_selector(locations[0], "text.html string.quoted"):
            # make sure it only triggers when: class="{here}"
            pt = locations[0] - len(prefix) - 1
            SEARCH_LIMIT = 250
            search_start = max(0, pt - SEARCH_LIMIT - len(prefix))
            line = view.substr(sublime.Region(search_start, pt))
            parts = line.split('=')
            if len(parts) > 2 and parts[-2].strip().endswith("class"):
                return self.class_completions
            else:
                return []
        elif view.match_selector(locations[0], "text.html meta.tag - text.html punctuation.definition.tag.begin"):
            # in tag: <div {here}>
            return self.attr_completions
        else:
            return []
