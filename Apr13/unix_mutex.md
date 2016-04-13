####Mutex

I'll quote a brilliant answer from stackoverflow:

>When I am having a big heated discussion at work, I use a rubber chicken which I keep in my desk for just such occasions. The person holding the chicken is the only person who is allowed to talk. If you don't hold the chicken you cannot speak. You can only indicate that you want the chicken and wait until you get it before you speak. Once you have finished speaking, you can hand the chicken back to the moderator who will hand it to the next person to speak. This ensures that people do not speak over each other, and also have their own space to talk.

Mutex is a *mutual exclusion* which ensuring that no two concurrent processes are in their *critical section* at the same time. *Critical section* is a period when the process accesses a shared resource, such as shared memory.

The requirement of mutual exclusion was identified and solved by E. Dijkstra in his [paper](http://www.di.ens.fr/~pouzet/cours/systeme/bib/dijkstra.pdf) Solution of a Problem in Concurrent Programming Control.
