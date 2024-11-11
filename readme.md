# Python WebSocket Server Template

Author: TJ S.

---

## Overview

This repository provides a simple **Python WebSocket server template** using the `websockets` library. It's designed as a boilerplate for developers to use as a reference or starting point for building WebSocket applications in Python. Alongside the server script, an HTML client is included to demonstrate communication with the server over a Local Area Network (LAN) using IP addresses.

## Features

- **WebSocket Server in Python**: A basic server implementation that listens for WebSocket connections and handles messages.
- **HTML Client Interface**: A simple web-based client with a terminal-like UI to send and receive messages.
- **LAN Compatibility**: Designed to work over a LAN without the need for domain names or SSL/TLS certificates.
- **Customizable**: Easily modify the server and client code to suit your application's needs.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Server](#running-the-server)
  - [Running the Client](#running-the-client)
- [Customization](#customization)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Getting Started

### Prerequisites

- **Python 3.6 or higher**
- **websockets library**: Install with `pip install websockets`
- **Web Browser**: Modern browser like Chrome, Firefox, or Edge

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/websocket-server-template.git
   cd websocket-server-template
   ```

2. **Install Dependencies**

   ```bash
   pip install websockets
   ```

---

## Usage

### Running the Server

1. **Configure the Server (if necessary)**

   - The server script `server.py` is set to listen on all network interfaces (`0.0.0.0`) and port `8765` by default.
   - If you need to change the port, edit the `start_server` line in `server.py`:

     ```python
     start_server = websockets.serve(handler, '0.0.0.0', YOUR_PORT_NUMBER)
     ```

2. **Start the Server**

   Run the server script:

   ```bash
   python server.py
   ```

   You should see:

   ```
   WebSocket server is running...
   ```

### Running the Client

1. **Configure the Client**

   - Open `index.html` in a text editor.
   - Replace `'192.168.1.100'` with your server's LAN IP address.
   - Ensure the port number matches the server's port.

     ```javascript
     const serverIp = 'YOUR_SERVER_IP'; // e.g., '192.168.1.100'
     const serverPort = '8765';         // Ensure this matches the server port
     ```

2. **Serve the HTML File**

   For the browser to run the WebSocket client properly, serve the `index.html` file using a local HTTP server:

   ```bash
   # Using Python 3's http.server module
   python -m http.server 8000
   ```

   - Navigate to `http://localhost:8000/` in your browser.

3. **Interact with the Server**

   - The client will attempt to connect to the WebSocket server upon loading.
   - Use the input box at the bottom to send messages.
   - Sent messages and server responses will appear in the terminal area.

---

## Customization

- **Server Logic**

  - Modify the `handler` function in `server.py` to implement custom message handling.
  - Example: Add conditional responses or integrate with other services.

- **Client Interface**

  - Edit `index.html` to change the look and feel of the client.
  - Customize the CSS styles in the `<style>` section.
  - Enhance functionality by adding more event handlers in the `<script>` section.

- **Port and IP Configuration**

  - Adjust the `serverPort` and `serverIp` variables in `index.html` and the `start_server` parameters in `server.py` to match your network setup.

---

## Security Considerations

- **LAN Usage**

  - This setup is intended for use within a trusted LAN environment.
  - Data transmitted is unencrypted (`ws://` protocol).

- **SSL/TLS for Public Networks**

  - If deploying over the internet or an untrusted network, implement SSL/TLS (`wss://` protocol).
  - Requires setting up SSL certificates and adjusting server and client code accordingly.

- **Firewall Settings**

  - Ensure that your system's firewall allows traffic on the specified port.
  - For testing purposes, you might need to disable or adjust firewall settings.

---

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request or open an issue.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or inquiries, please contact **TJ S**.

- **GitHub**: [tajulsharby](https://github.com/tajulsharby/)

---

**Happy Coding!**

---

*This README was generated to assist developers in understanding and utilizing the Python WebSocket server template provided.*