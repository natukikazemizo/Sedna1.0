```mermaid
classDiagram
  direction LR
  class Client
  class Facade {
    -linksToSubsystemObjects
    -optionalAdditionalFacade
    +subsystemOperation()
  }
  class AdditionalFacade {
    +anotherOperation()
  }
namespace ManySubsystems {
  class SubsystemA
  class SubsystemB
  class SubsystemC
}
  Client --> Facade
  Facade --> AdditionalFacade
  Facade ..> SubsystemA
  Facade ..> SubsystemB
  AdditionalFacade ..> SubsystemB
  AdditionalFacade ..> SubsystemC
 
 ```