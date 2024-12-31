# **MarketOps: A Distributed Financial Market Simulation Framework**

## **Overview**

MarketOps is a high-performance, distributed financial market simulation framework built with **Go** and powered by **gRPC**. It enables seamless interaction with simulated financial instruments, order books, and real-time analytics. The framework supports dynamic administration via SSH, web-based interfaces, and terminal-based clients. It is fully containerized with Docker for portability and scalability.

---

## **Features**

1. **Market Server**:
   - Manage financial instruments (e.g., equities, options).
   - Place and query orders in a simulated order book.

2. **Analytics Server**:
   - Provides real-time price summaries and volume trends.
   - Analyze historical trading data for trends and insights.

3. **Web Front-End**:
   - User-friendly web interface for managing instruments and orders.
   - Built with Flask and supports interaction with the Market Server.

4. **Terminal Client**:
   - Command-line client for advanced users to interact with the servers.

5. **Admin SSH Service**:
   - Securely halt/resume trading or issue administrative commands via SSH.

6. **Containerization**:
   - Dockerized setup ensures portability and easy deployment across environments.

7. **Scalability**:
   - Modular architecture allows deployment of individual services on distributed systems.

---

## **Architecture**

```
MarketOps/
├── proto/                    # gRPC Protobuf definitions
│   ├── market.proto          # Market service definitions
│   ├── analytics.proto       # Analytics service definitions
├── server/                   # Go-based gRPC servers
│   ├── market_server.go      # Market server implementation
│   ├── analytics_server.go   # Analytics server implementation
├── client/                   # Go-based clients
│   ├── market_client.go      # Terminal-based client
│   ├── web/                  # Web front-end
│       ├── app.py            # Flask application
│       ├── templates/        # HTML templates for the web app
├── admin/                    # SSH admin service
│   ├── Dockerfile            # SSH admin Dockerfile
├── shared/                   # Shared resources (e.g., admin commands file)
│   ├── admin_commands.txt    # File for admin commands
├── Dockerfile                # Dockerfile for Go services
├── docker-compose.yml        # Docker Compose configuration
└── README.md                 # Comprehensive project documentation
```

---

## **Setup and Installation**

### **1. Prerequisites**
- **Go**: Version 1.18+.
- **Protobuf Compiler (`protoc`)**: Install [here](https://grpc.io/docs/protoc-installation/).
- **Docker**: Install [here](https://docs.docker.com/get-docker/).

---

### **2. Setup the Project**

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd MarketOps
   ```

2. **Generate gRPC Code**:
   Compile `.proto` files to generate Go bindings:
   ```bash
   protoc --go_out=. --go-grpc_out=. proto/market.proto
   protoc --go_out=. --go-grpc_out=. proto/analytics.proto
   ```

3. **Build Docker Images**:
   Use Docker Compose to build all services:
   ```bash
   docker-compose build
   ```

---

### **3. Running the Application**

1. **Start All Services**:
   Launch the servers, client, and SSH service:
   ```bash
   docker-compose up
   ```

2. **Access the Application**:
   - **Web Interface**: Open [http://localhost:5000](http://localhost:5000) in your browser.
   - **Terminal Client**:
     ```bash
     go run client/market_client.go
     ```
   - **Admin SSH**:
     ```bash
     ssh root@localhost -p 2222
     Password: adminpassword
     ```
     Halt trading:
     ```bash
     echo "halt" > shared/admin_commands.txt
     ```

3. **Stop All Services**:
   ```bash
   docker-compose down
   ```

---

## **Technical Highlights**

1. **Concurrency**:
   - Go’s goroutines ensure efficient handling of multiple client requests.
   - Mutexes ensure thread-safe operations on shared resources like the order book.

2. **Scalability**:
   - gRPC-based communication supports high-throughput, low-latency data exchange.
   - Containerized services enable horizontal scaling across distributed environments.

3. **Flexibility**:
   - Supports both web and terminal-based clients.
   - Admin SSH service allows secure real-time control.

4. **Modularity**:
   - Separate servers for market and analytics functionality.
   - Independent deployment and scaling of services.

---

## **Contribution**
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---

## **Future Enhancements**
- Add support for complex financial derivatives (e.g., futures, swaps).
- Introduce authentication for the web and SSH services.
- Enhance analytics with machine learning models for trend prediction.
