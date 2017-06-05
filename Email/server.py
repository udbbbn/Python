# -*- coding:utf-8 -*-
#启动Web服务器

from http.server import HTTPServer, CGIHTTPRequestHandler
import http

port = 8090

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('Starting simple_httpd on port:' + str(httpd.server_port))
httpd.serve_forever()

    

