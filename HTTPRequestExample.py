import urllib.request, json

# Pretty Print
import pprint

pp = pprint.PrettyPrinter(indent=4)


# valid json-string??
def is_json(myjson):
    try:
        _ = json.loads(myjson)
    except ValueError:
        return False
    return True


def framed_box(text):
    laenge = 62 + len(text)
    print(laenge * "=")
    print(30 * "=" + " " + text + " " + 30 * "=")
    print(laenge * "=")


def http_client_get():
    url = "https://httpbin.org/get"
    # HTTP Request
    with urllib.request.urlopen(url) as response:
        # read header
        # print(response.headers)

        # read response
        response_data = response.read().decode()
        # if json string?
        if is_json(response_data):
            json_data = json.loads(response_data)
            pp.pprint(json_data)
        else:
            print(response_data)


def http_client_get_with_data():
    url = "https://httpbin.org/get"

    get_values = {'value1': 'hello',
                  'Value2': 'Olli'}
    url_values = urllib.parse.urlencode(get_values)

    # full url
    url_with_data = url + '?' + url_values
    with urllib.request.urlopen(url_with_data) as response:
        # read response
        response_data = response.read().decode()
        # if json string?
        if is_json(response_data):
            json_data = json.loads(response_data)
            pp.pprint(json_data)
        else:
            print(response_data)


def http_client_post():
    url = "http://httpbin.org/post"

    # post data
    post_values = {'value1': 'hello',
                   'Value2': 'Olli'}
    data = urllib.parse.urlencode(post_values)
    # data should be bytes
    data = data.encode('UTF-8')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        # read response
        response_data = response.read().decode()
        # if json string?
        if is_json(response_data):
            json_data = json.loads(response_data)
            pp.pprint(json_data)
        else:
            print(response_data)


if __name__ == '__main__':
    framed_box("Test GET")
    http_client_get()
    framed_box("Test GET /w Attr")
    http_client_get_with_data()
    framed_box("Test Post /w Attr")
    http_client_post()
