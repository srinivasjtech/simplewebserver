from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
       
    </head>
    <body>
        <h1 align="center"> Device Specification-25015562</h1>
        <table border="6" align="center" >
            <tr>
                <th>No.</th>
                <th>Name</th>
                <th>SSD</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Lenovo</td>
                <td>512GBD</td>
            </tr>
            <tr>
                <td>2</td>
                <td>acer</td>
                <td>512GB</td>
            </tr>
            <tr>
                <td>3</td>
                <td>HP</td>
                <td>1TB</td>
            </tr>
            <tr>
                <td>4</td>
                <td>asus</td>
                <td>128GB</td>
            </tr>
            <tr>
                <td>5</td>
                <td>lenovo thinkpad</td>
                <td>256GB</td>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()