# Python Messaging App

It is an application for using FCM for simple messaging interchanges. For the FCM integration it uses node. For deliver to clients it uses Flask + WebSockets.

## Requeriments
* Node v8
* Firebase sender id
* Firebase serverKey
* Python 3

## Installation
`pip install flask flask_socketio`

`yarn install`

## Set up

It is needed to set up an toList.js file containing the FCM destination devices.

```["device_id1", "device_id2", ...]```

It is needed set up the FCM ApiKey and SenderID in the environment variables. And also the server port.

```
ApiKey=FCMAPIKEY
```

```
SenderID=NumericalSenderID
```

```
PORT=5000
```

If no credentials are set up, it will get one from FCM using your ApiKey and SenderId. It structure is the following:

```
{
    "keys": {
        "privateKey":PRIVATEKEY,
        "publicKey":PUBLICKEY,
        "authSecret":AUTHSECRET
    },
    "fcm": {
        "token": FCMTOKEN,
        "pushSet": FCMPUBLISHSET
    },
    "gcm": {
        "token": GCMTOKEN,
        "androidId": GCMANDROIDID,
        "securityToken": GCMSECURITYTOKEN,
        "appId": APPID
    }
```