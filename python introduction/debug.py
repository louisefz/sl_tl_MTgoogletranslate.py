Traceback (most recent call last):
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/urllib3/connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/urllib3/util/connection.py", line 96, in create_connection
    raise err
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/urllib3/util/connection.py", line 86, in create_connection
    sock.connect(sa)
OSError: [Errno 113] No route to host

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 382, in _make_request
    self._validate_conn(conn)
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 1010, in _validate_conn
    conn.connect()
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/urllib3/connection.py", line 358, in connect
    conn = self._new_conn()
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/urllib3/connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPSConnection object at 0x7f390dc4a1c0>: Failed to establish a new connection: [Errno 113] No route to host

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/requests/adapters.py", line 439, in send
    resp = conn.urlopen(
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 755, in urlopen
    retries = retries.increment(
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/urllib3/util/retry.py", line 574, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='www.theguardian.com', port=443): Max retries exceeded with url: /international (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f390dc4a1c0>: Failed to establish a new connection: [Errno 113] No route to host'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "webscraping.py", line 24, in <module>
    r_guardian_homepage = requests.get('https://www.theguardian.com/international')
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/requests/api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/requests/sessions.py", line 542, in request
    resp = self.send(prep, **send_kwargs)
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/requests/sessions.py", line 655, in send
    r = adapter.send(request, **kwargs)
  File "/python_project/wechat_project/wechat1_venv/lib/python3.8/site-packages/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='www.theguardian.com', port=443): Max retries exceeded with url: /international (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f390dc4a1c0>: Failed to establish a new connection: [Errno 113] No route to host'))