# Apache Log Analyzer

The **Apache Log Analyzer** is a Python tool that proccesses Apache-style access logs.

It extracts and tracks key information **per IP address**:
- **IP Address** - the client making the request
- **HTTP Methods** - e.g., `POST`, `GET`, `DELETE`
- **Resources Requested** - pages, endpoints, or files accessed
- **Entry Count** - total number of log entries recorded for that IP