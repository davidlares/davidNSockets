# davidNSockets

This is a simple repository for demonstrating the very basics on network socket programming with Python3.

Let's review a little bit when we talk about sockets we actually define it as a communications mechanism that allows clients/serves to connect to each other with specific rules

Socket Programming is a way of connecting two nodes on a network to communicate with each other, basically, the server forms the listener socket while the client reaches out to the server.

## Socket LifeCycle

For the server side of the Socket, the process starts while back, because the server itself creates and starts the socket, binds the connection string and sets the logic for handling clients

  Socket -> Set Socket Options -> Bind -> Listen -> Accept -> Send/Receive

On the other hand, the client has the simplest creation form.

  Socket -> connect (where is listening) -> Send/Receive information

## Virtualenv

For these examples, you don't actually need to install any specific dependencies, I use only the native socket module from the python language.

## Usage

You will find 3 folders, two for `UDP` and `TCP` protocols and third `raw` folder is for RAW sockets.

The `TCP` folder has a `clients.py` and a `server.py`, very clear on what roles accomplish each one. Just run the python scripts like `python3 [filename.py]`. You will need to open two terminals for viewing the message received and sent by the client and the servers.

The `UDP` folder is almost the same run process of the `TCP`, internally things change a little because of the protocol.

For the `raw` protocol things are different, the `raw.py` scripts let the host (FOR ALL is LOCALHOST IP), but this script works like a `network sniffer`, you just can `ping 127.0.0.1` and you will see a stream of data sent to the raw Socket server.

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
