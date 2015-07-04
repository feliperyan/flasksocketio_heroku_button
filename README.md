#Simple example of using Flask and SocketIO on Heroku.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/feliperyan/flasksocketio_heroku_button)

You can use curl to send messages to the server which will be reflected live on index.html

```
curl -i -H "Content-Type: applicatio/json" -X POST -d '{"message":"Read a book"}' http://localhost:5000/api/v1.0/scans
```