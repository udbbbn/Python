# -*- coding:utf-8 -*-

#启动web服务器

from http.server import HTTPServer,CGIHTTPRequestHandler

port = 8090

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('Starting simple_httpd on port:' + str(httpd.server_port))
httpd.serve_forever()