```mermaid
---
title: Composition：コンポジット
config:
---
classDiagram
    direction TB
 
    class Fox {
        +run()
    }



    class Tail {
        +wave()
    }


 
    Fox *-- Tail


```