## Latency
The time from the source sending a packet to the destination receiving it. There is two parts related to the speed: latency and bandwidth. Internet connection can be 'fast' but in the same time response time might be slow.

Final latency is a sum of the all network layers. Usually most slowest layer is the 'last mile', from ISP to your machine.

#### Layers
`User -> wifi -> cable -> ISP -> (optical fibre) -> ISP -> Ethernet -> Server`. Last mile is a distance between ISP to end point. All of these layers have a their own latency.

#### Fiber lantency

```
+-----------+---------------+----------+-------------+--------------+
| From      | To            | Distance | Time(light) | Time(fiber)  |
=====================================================================
| New York  | San Francisco | 4,148km  | 14ms        | 42ms         |
|-----------+---------------+----------+-------------+--------------+
| New York  | London        | 5,585km  | 19ms        | 56ms         |
+-----------+---------------+----------+-------------+--------------+
```

Fiber speed is a something between 1.4 - 1.6 slower than speed of light. However, minimum latency from New York to London is 56ms. All these numbers is ideal and non-realistic. They calculated acording to 'shortest route' which is usually not the case. Packets travels in non optimal ways.

#### CND
The obvious solution to reduce transportation latency is to locate server with a content closer to the users. Content delivery network services provide many benefits, but most useful among them is the closer location to the end user.
