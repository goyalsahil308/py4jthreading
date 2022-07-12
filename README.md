# py4jthreading

### 1.There are 5 functions in java program. First 3 functions(multi, multi2 and divi) give response to python functions(multiply, multiply2 and division)
### 2.From python functions  three calls are made to three java functions using gateway
### 3.Another 2 functions of java (resp and sum) make call to python program(response2 and plus) and take result. But we have to call these 2 java functions from python first.There calls are made by python functions(response and sumjava)
### 4.Now we make all python functions thread Now 3 calls are made from python to java and 2 calls from java to python are made .There all 5 calls are made concurrently using threads
### 5.The pythons program will give its output in python terminal and java program will give its output it java terminal. 
  
# Py4J Threading and connection model
### In its default mode, Py4J allocates one thread per connection. The design of Py4j is symmetrical on the Python and Java sides. A Python GatewayClient communicates with the Java GatewayServer and is then associated with a GatewayConnection. A Java CallbackClient (for callbacks) communicates with the Python CallbackServer and is then associated with a CallbackConnection. A connection runs in the calling thread.

And now, for the details:

## On the Python side: calling Java

Py4J on the Python side does not explicitly create a thread to call Java methods. When a method is called, a connection to the Java GatewayServer is established
in the calling thread. If multiple threads are calling Java methods concurrently, Py4J will ensure that each thread has its own connection by requesting more
connections.
To be extra clear: if you only call Java, Py4J on the Python side will never create a thread.
To be extra extra clear: Py4J is thread-safe so if you use a JavaGateway from multiple threads that you created, Py4J will make manage the network resources 
appropriately.

## On the Python side: receiving callbacks from Java

Py4J explicitly creates a thread to run the CallbackServer, which accepts callback connection requests, and a thread for each callback connection request.
As long as there is no concurrent callback from the Java side, the same callback connection/thread will be used.
These threads are necessary to prevent deadlocks. For example, if we only had a single thread to handle callbacks from Java, Py4J would deadlock as soon as it would
encounter an indirect recursion between Java and Python functions. Early versions of Py4J made this mistake :-)

## On the Java side: receiving calls from Python

Py4J explicitly creates a thread to run the GatewayServer, which accepts connection requests (from a GatewayClient), and a thread for each connection request. 
As long as there is no concurrent call from the Python side, the same connection/thread will be used.

## On the Java side: calling back Python

Py4J on the Java side does not explicitly create a thread to make a callback to a Python object. When a callback is called, a connection to the CallbackServer is
established in the calling thread. If you created multiple threads in Java to call back Python concurrently, Py4J will ensure that each thread has its own
CallbackConnection.

For more information visit: https://www.py4j.org/advanced_topics.html
