```mermaid
classDiagram
  direction TB
  class ServiceInterface {
    <<interface>>
    +operation()
  }
  class Proxy {
    -realService: Service
    +Proxy(s: Service)
    +checkAccess()
    +operation()
  }
  class Service {
    ...
    +operation()
  }
  note for Proxy "realService = s"
  note for Proxy "+operation():
  if (checkAccess()) {
    &nbsp&nbsp&nbsprealService.operation()
  }"
  Client --> ServiceInterface
  ServiceInterface <|.. Proxy  
  ServiceInterface <|.. Service
  Proxy o--> Service
 ```