SimpleKV
========

This is a simple Redis backed REST kv store. Data are deleted after 6 months
without being read or written to. No auth, nothing.

```
# store data
curl -X POST <url>/some_key/name -d data=hello
# retrieve data
curl <url>/some_key/name
```
