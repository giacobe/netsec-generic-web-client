# NetSurf 3.10 GTK resources include XPM icons. GdkPixbuf 2.42.12 disables
# those loaders by default, so enable them for both resource generation and
# the guest's GTK image loading.
HOST_GDK_PIXBUF_CONF_OPTS += -Dothers=enabled
GDK_PIXBUF_CONF_OPTS += -Dothers=enabled
