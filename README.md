# APIs

## Introduction

### What is an API?

An API is an application programming interface. It is a set of functions and procedures that allow the creation of applications that access the features or data of an operating system, application, or other service, without having to know the underlying code or implementation.

### What is a RESTFUL API?

REST stands for REpresentational State Transfer. It is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other. REST-compliant systems, often called RESTful systems, are characterized by how they are stateless and separate the concerns of client and server. In REST, a resource is an object or representation of something, which has associated data with it. Resources are accessed and manipulated using a set of common operations, which are HTTP methods: GET, POST, PUT, PATCH, and DELETE. These operations are applied to a resource's identifier to produce a result in the form of another resource, often with the appropriate HTTP response code.

### Why is JSON used in RESTFUL APIs?

JSON is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language Standard ECMA-262. JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language.

The systanx of JSON is derived from JavaScript object notation syntax, but the JSON format is text only. Code for reading and generating JSON data can be generated in many programming languages.

```json
{
    "key": "value"
}
```

```json
{
  "name": "Abishek Annese",
  "age": 43,
  "address": {
    "streetAddress": "19 London Road",
    "city": "Portsmouth",
    "state": "Hampshire",
    "postalCode": "PO1 2AB"
  },
  "phoneNumber": [
    {
      "type": "Home",
      "number": "02392123456"
    },
    {
      "type": "Work",
      "number": "07450123456"
    }
  ]
}
```

### What are the HTTP methods?

HTTP methods are used to perform different operations on a resource. The most common methods are GET, POST, PUT, and DELETE. The methods are case-sensitive and should be treated as such.

| Method | Description |
| ------ | ----------- |
| GET | The GET method requests a representation of the specified resource. Requests using GET should only retrieve data. |
| POST | The POST method is used to submit an entity to the specified resource, often causing a change in state or side effects on the server. |
| PUT | The PUT method replaces all current representations of the target resource with the request payload. |
| DELETE | The DELETE method deletes the specified resource. |

## Python APIs

### Why Learn Rest API with Python?

Python is a general-purpose programming language that is becoming more and more popular. It is used in a wide variety of fields, including web development, data science, and machine learning. Python is a great language to learn because it is easy to read and write, and it is very powerful. It is also very popular, so there are many resources available to help you learn it.

### Why Python Is a Good Language for Developing Rest API?

- easy to use syntax
- has wide range of applications for web development i.e. Django, Flask, etc.