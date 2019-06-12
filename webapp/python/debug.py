from app import app
from wsgi_lineprof.middleware import LineProfilerMiddleware
from wsgi_lineprof.filters import FilenameFilter, TotalTimeSorter


if __name__ == '__main__':
    #app.app.run(port=5000, debug=True, threaded=True)

    filters = [
            FilenameFilter("/home/isucon/isubata/webapp/python/app.py"),
            TotalTimeSorter(),
            ]
    with open("/home/isucon/isubata/webapp/python/lineprof.log", "w") as f:
        app.wsgi_app = LineProfilerMiddleware(app.wsgi_app, stream=f, filters=filters)
        app.run(port=5000, debug=True, threaded=True)
