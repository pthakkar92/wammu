from django.conf.urls.defaults import *
from news.feeds import RssNewsFeed, AtomNewsFeed
from phonedb.feeds import RssPhonesFeed, AtomPhonesFeed

newsfeeds = {
    'rss': RssNewsFeed,
    'atom': AtomNewsFeed,
}

phonesfeeds = {
    'rss': RssPhonesFeed,
    'atom': AtomPhonesFeed,
}

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^wammu/', include('wammu.foo.urls')),
    (r'^$', 'wammu.views.index'),
    (r'^gammu/$', 'wammu.views.gammu'),
    (r'^smsd/$', 'wammu.views.smsd'),
    (r'^wammu/$', 'wammu.views.wammu'),
    (r'^libgammu/$', 'wammu.views.libgammu'),
    (r'^python-gammu/$', 'wammu.views.pygammu'),

    (r'^authors/$', 'wammu.views.static', {'page': 'authors.html'}),
    (r'^license/$', 'wammu.views.static', {'page': 'license.html'}),
    (r'^search/$', 'wammu.views.static', {'page': 'search.html'}),

    (r'^support/$', 'wammu.views.static', {'page': 'support/index.html'}),
    (r'^support/bugs/$', 'wammu.views.static', {'page': 'support/bugs.html'}),
    (r'^support/lists/$', 'wammu.views.static', {'page': 'support/lists.html'}),
    (r'^support/online/$', 'wammu.views.static', {'page': 'support/online.html'}),
    (r'^support/buy/$', 'wammu.views.static', {'page': 'support/buy.html'}),

    (r'^contribute/$', 'wammu.views.static', {'page': 'contribute/index.html'}),
    (r'^contribute/code/$', 'wammu.views.static', {'page': 'contribute/code.html'}),
    (r'^contribute/translate/$', 'wammu.views.static', {'page': 'contribute/translate.html'}),
    (r'^contribute/publicity/$', 'wammu.views.static', {'page': 'contribute/publicity.html'}),

    (r'^docs/$', 'wammu.views.static', {'page': 'docs/index.html'}),
    (r'^docs/man/$', 'manpages.views.show_pages'),
    (r'^docs/man/(?P<lang>[a-z]*)/$', 'manpages.views.show_lang_pages'),
    (r'^docs/man/(?P<lang>[a-z]*)/(?P<page>[a-z_-]*\.[0-9])/$', 'manpages.views.show_page'),
    (r'^docs/devel/$', 'wammu.views.static', {'page': 'docs/devel.html'}),

    # RSS feeds
    (r'^news/(?P<url>(rss|atom).*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': newsfeeds}),

    # News
    (r'^news/$', 'news.views.index'),
    (r'^news/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[^/]*)/$',
        'news.views.entry'),
    (r'^news/(?P<slug>.*)/$', 'news.views.category'),

    (r'^download/$', 'downloads.views.download'),
    (r'^download/(?P<program>[^/]*)/$', 'downloads.views.program'),
    (r'^download/(?P<program>[^/]*)/(?P<version>[0-9.]*)/$', 'downloads.views.release'),
    (r'^download/(?P<program>[^/]*)/(?P<platform>[^/]*)/$', 'downloads.views.list'),

    # RSS feeds
    (r'^phones/(?P<url>(rss|atom).*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': phonesfeeds}),
    (r'^phones/csv/$', 'phonedb.views.phones_csv'),

    # Phone database
    (r'^phones/$', 'phonedb.views.index'),
    (r'^phones/new/$', 'phonedb.views.create'),
    (r'^phones/new-wammu/$', 'phonedb.views.create_wammu'),
    (r'^phones/search/$', 'phonedb.views.search'),
    (r'^phones/search/(?P<featurename>[^/]*)/$', 'phonedb.views.search'),
    (r'^phones/(?P<vendorname>[^/]*)/$', 'phonedb.views.vendor'),
    (r'^phones/(?P<vendorname>[^/]*)/(?P<id>[0-9]*)/$', 'phonedb.views.phone'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Media files
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': './media'}),


    # Donations
    (r'^donate/$', 'donate.views.donate'),
    (r'^donate/thanks/$', 'donate.views.thanks'),

    # Screenshots
    (r'^screenshots/$', 'screenshots.views.index'),
    (r'^screenshots/(?P<slug>.*)/$', 'screenshots.views.category'),

    # Links
    (r'^links/$', 'links.views.index'),

    # Compatibility
    (r'^install/$', 'django.views.generic.simple.redirect_to', {'url': '/download/'}),
    (r'^improve/$', 'django.views.generic.simple.redirect_to', {'url': '/contribute/'}),
)
