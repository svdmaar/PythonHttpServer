import http.server
import socketserver

port = 8080

class MyHttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        responsePrefix ="/response.html?" 
        if self.path == "/":
            # TODO: real "redirect"
            self.path = "/index.html"
            super().do_GET()
        elif self.path.startswith(responsePrefix):
            queryString = self.path[len(responsePrefix):]
            dataFields = queryString.split("&")
            sum = 0
            infoStr = ""
            try:
                for dataField in dataFields:
                    numberStr = dataField.split("=")[1]
                    number = int(numberStr)
                    sum += number
                    infoStr += dataField + "<br/>\n"
            except Exception as error:
                infoStr = str(error)
            else:
                infoStr += "sum: " + str(sum) + "<br/>\n"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = "<html><head><title>Result</title><body><p>" + infoStr + "</p></body></html>"
            self.wfile.write(bytes(html, "utf8"))
        else:
            super().do_GET()

with socketserver.TCPServer(("", port), MyHttpHandler) as httpd:
    httpd.serve_forever()

