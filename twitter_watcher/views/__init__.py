# -*- coding: utf-8 -*-


def register_blueprints(app):
	# Prevents circular imports
    from twitter_watcher.views.listener import listeners_view
    from twitter_watcher.views.healthcheck import healthcheck
    app.register_blueprint(listeners_view)
    app.register_blueprint(healthcheck)
