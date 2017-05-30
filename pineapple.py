import StringIO
from flask import Flask, send_file, request

from xhtml2pdf import pisa

import urllib2


app = Flask(__name__)


@app.route('/pdf/')
def hello_pdf():
    pisa.showLogging()

    packet = StringIO.StringIO()
    sourcehtml = "<html><body><p>To PDF or not to PDF<p></body></html>"
    
    if (request.values.has_key("url")):    
		print request.values["url"]
		url = urllib2.urlopen(request.values["url"])
		sourcehtml = url.read()
    
    pisa.CreatePDF(
        sourcehtml,
        dest=packet,
        show_error_as_pdf=True)

    packet.seek(0)
    return send_file(packet, attachment_filename="result.pdf", as_attachment=False)



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
