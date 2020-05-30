const request = require('request');
const fs = require('fs');
const { register, listen } = require('push-receiver');

function readCredentials(){
  return JSON.parse(fs.readFileSync('credentials.json', 'utf-8'));
}

function storeCredentials(credentials){
  fs.writeFileSync('credentials.json', JSON.stringify(credentials));
}

async function newCredentials(){
  const credentials = await register(process.env.SenderID);
  storeCredentials(credentials);
  return credentials;
}

function onNotification({ notification, persistentIds }) {
  request.post('http://127.0.0.1:5000/receive',
  {
    json: {
      message: notification.notification.body
    }
  }, (error, res, body) => {
    if (error) {
      console.error(error)
      return
    }
    console.log(`statusCode: ${res.statusCode}`)
    console.log(body)
  });
}

async function getNotif(credentials){
  const persistentIds = [];
  await listen({...credentials, persistentIds}, onNotification)
}

async function main(){
  let credentials;
  try{
    credentials = readCredentials();
  } catch(error){
    credentials = await newCredentials();
  }
  await getNotif(credentials);
}

main();