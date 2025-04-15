```mermaid
---
title: Dependency：依存
config:
---
classDiagram
    class Velocity {
        -x
        -y
        -z
    }

    class Fox {
        +run()
        +getSpeed()Velocity
    }

 
    Fox ..> Velocity

```