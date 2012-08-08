# -*- coding:utf-8 -*-
import re

from django.conf.urls.defaults import *
import pingdjack

from marcus import views, models, feeds

urlpatterns = patterns('',
    url(r'^(?:(en|ru)/)?$', views.index, name='marcus-index'),

    url(r'^category/(?:(en|ru)/)?$', views.category_index, name='marcus-categories'),
    url(r'^category/([A-Za-z0-9_-]+)/(?:(en|ru)/)?$', views.category, name='marcus-category'),
    url(r'^archive/(?:(en|ru)/)?$', views.archive_index, name='marcus-archive-index'),
    url(r'^archive/(\d{4})/(?:(\d{2})/)?(?:(en|ru)/)?$', views.archive, name='marcus-archive'),

    url(r'^suspected/$', views.spam_queue, name='marcus-spam-queue'),
    url(r'^suspected/approve/(\d+)/$', views.approve_comment, name='marcus-approve-comment'),
    url(r'^suspected/spam/(\d+)/$', views.spam_comment, name='marcus-spam-comment'),
    url(r'^suspected/delete/$', views.delete_spam, name='marcus-delete-spam'),

    url(r'^feed/(?:(en|ru)/)?$', feeds.Article(), name='marcus-feed'),
    url(r'^^category/([A-Za-z0-9_-]+)/feed/(?:(en|ru)/)?$', feeds.Category(), name='marcus-category-feed'),
    url(r'^comments/feed/(?:(en|ru)/)?$', feeds.Comment(), name='marcus-comments-feed'),
    url(r'^(\d{4})/(\d{2})/(\d{2})/([^/]+)/feed/(?:(en|ru)/)?$', feeds.ArticleComment(), name='marcus-article-comments-feed'),

    url(r'^comment_preview/$', views.comment_preview, name='marcus-comment-preview'),
    url(r'^pingback/$', pingdjack.server_view, name='marcus-pingback'),

    url(r'^(\d{4})/(\d{2})/(\d{2})/([^/]+)/(?:(en|ru)/)?$', views.article, name='marcus-article'),
    url(r'^draft/(\d+)/(?:(en|ru)/)?$', views.draft, name='marcus-draft'),
    url(r'^([^/]+)/$', views.find_article, name='marcus-find-article'),
)
