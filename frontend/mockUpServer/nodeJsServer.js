const WebSocket = require('ws');
 
const server = new WebSocket.Server({ port: 8080 });
 
server.on('connection', socket => {
  socket.on('message', message => {
    console.log(`received from a client: ${message}`);
  });
  socket.send('Hello world from NodeJS Server to Kitchen Appliance Frontend :)');
});