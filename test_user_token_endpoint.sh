#! /usr/bin/bash
curl -X POST --header 'Content-Type: application/json' --data '{"username":"nolimax", "password":"admin"}' http://127.0.0.1:8000/user/api/token/