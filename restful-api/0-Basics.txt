# Basics of HTTP/HTTPS

## Definition

***HTTP(S)***
.H > Hyper
.T > Text
.T > Transfer
.P > Protocol
.S > Secure

## 1-Difference

HTTPS is a secure version of HTTP that allows each step on a web page to be verified,
so HTTPS is more secure than HTTP.

<img src ="https://www.cloudflare.com/img/learning/security/glossary/what-is-ssl/http-vs-https.svg">

## 2-A depiction or outline HTTP

HTTP is a protocol for retrieving resources such as HTML documents.
It is the basis for all data exchange on the Web.
It is a client-server protocol, which means that requests are initiated by the recipient
(usually a web browser).
A complete document is constructed from various sub-documents that are retrieved,
for example text, layout descriptions, images, videos, scripts and much more.

<img src ="https://developer.mozilla.org/fr/docs/Web/HTTP/Overview/fetching_a_page.png">


## 3-Lists of common HTTP methods and status codes

HTTP request methods

These are the nine HTTP methods typically associated with RESTful web development and the Hypertext Transfer Protocol and most commonly used by RESTful API designers:

### ***GET.***

The purpose of the GET method is to simply retrieve data from the server. The GET method is used to request any of the following resources:

. A webpage or HTML file.
. An image or video.
. A JSON document.
. A CSS file or JavaScript file.
. An XML file.

### ***PUT.***

The HTTP PUT method is used to completely replace a resource identified with a given URL.

The HTTP PUT request method includes two rules:

A PUT operation always includes a payload that describes a completely new resource definition to be saved by the server.
The PUT operation uses the exact URL of the target resource.
If a resource exists at the URL provided by a PUT operation, the resource’s representation is completely replaced. If a resource does not exist at that URL, a new resource is created.

The payload of a PUT operation can be anything that the server understands, although JSON and XML are the most common data exchange formats for RESTful webservices and microservices.

### ***POST.***

The POST HTTP request method sends data to the server for processing.

The data sent to the server is typically in the following form:

. Input fields from online forms.
. XML or JSON data.
. Text data from query parameters.

### ***DELETE.***

The HTTP DELETE method is self-explanatory. After execution, the resource a DELETE operation points to is removed from the server.

### ***PATCH.***

Sometimes object representations get very large. The requirement for a PUT operation to always send a complete resource representation to the server is wasteful if only a small change is needed to a large resource.

The PATH HTTP method, added to the Hypertext Transfer Protocol independently as part of RFC 5789, allows for updates of existing resources. It is significantly more efficient, for example, to send a small payload rather than a complete resource representation to the server.

### ***HEAD.***

The HTTP HEAD method simply returns metadata about a resource on the server. This HTTP request method returns all of the headers associated with a resource at a given URL, but does not actually return the resource.

The HTTP HEAD method is commonly used to check the following conditions:

The size of a resource on the server.
If a resource exists on the server or not.
The last-modified date of a resource.
Validity of a cached resource on the server.
The following example shows sample data returned from a HEAD request:

```
HTTP/1.1 200 OK
Date: Fri, 19 Aug 2023 12:00:00 GMT
Content-Type: text/html
Content-Length: 1234
Last-Modified: Thu, 18 Aug 2023 15:30:00 GMT
```
### ***OPTIONS.***

The server does not have to support every HTTP method for every resource it manages.

Some resources support the PUT and POST operations. Other resources only support GET operations.

The HTTP OPTIONS method returns a listing of which HTTP methods are supported and allowed.

The following is a sample response to an HTTP OPTIONS method call to a server:
```
OPTIONS /example/resource HTTP/1.1
Host: www.example.com HTTP/1.1 200 OK
Allow: GET, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, DELETE, OPTIONS
Access-Control-Allow-Headers: Authorization, Content-Type
```

### ***TRACE.***

The TRACE HTTP method is used for diagnostics, debugging and troubleshooting. It simply returns a diagnostic trace that logs data from the request-response cycle.

The content of a trace is often just an echo back from the server of the various request headers that the client sent.

### ***CONNECT.***

The connect operation is used to create a connection with a server-side resource. The most common target of the HTTP method CONNECT is a proxy server, which a client must access to tunnel out of the local network.

RESTful API designers rarely interact with the CONNECT HTTP request method


## Status codes

The most common codes are:

200: request success;
301 and 302: redirect, permanent and temporary respectively;
401: unauthenticated user;
403: access denied;
404: resource not found;
500, 502 and 503: server errors;
504: The server did not respond.
