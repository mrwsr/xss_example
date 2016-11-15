from django.http import HttpResponse


SUBMIT_PAGE = """
<html>
    <form action="/xss/response" method="POST">
      <label>
        Enter something
        <input name="something" type="text"></input>
      </label>
    </form>
</html>
"""


RESPONSE_TEMPLATE = """
<html>
   You entered: {something}
   <a href="/xss/submit">Do it again</a>
</html>
"""


def xss_submit(request):
    assert request.method == "GET"
    return HttpResponse(SUBMIT_PAGE, content_type="text/html")


def xss_response(request):
    assert request.method == "POST"
    something = request.POST.get(u"something",
                                 u"None").encode('utf-8')

    rendered = RESPONSE_TEMPLATE.format(something=something)
    print rendered
    return HttpResponse(rendered, content_type="text/html")
