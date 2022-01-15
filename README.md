# Cache-Management

## Background:

In computers, memory is located in different parts of the computer; memory on disk is far away from the CPU and takes a long time to access, but offers a large amount of storage; cache memory is close to the CPU so it is faster to access, but does not offer a lot of storage space.
It is therefore wise to use the cache memory in a smart way, so that pages of memory that are more likely to be accessed are already in the cache. This means that there are fewer accesses to disk memory, and the memory transaction is ultimately quicker.
In this program, we will use Python to simulate a cache with two management techniques, which are explained below. 

The cache memory operates in the following manner:
Pages from memory are requested. When a page from memory is requested, the cache memory is searched for that page. 
If the page is found in the cache memory, then this is called a "hit". If the page is not found in the cache memory, then this is called a "miss".
When a miss happens, the page must be retrieved from the main memory (the disk memory) and must be placed in the cache memory. If the cache memory is not full, then the page is simply added to the cache memory. If the cache memory is full, then one of the pages that is in the cache memory will have to be replaced. In this case, we say that a new page is added to the cache memory, and the old page is evicted. There are multiple ways in which we can choose which page to evict.
Two of those are presented below, the "First in First Out (FIFO)" algorithm, and the "Least Frequently Used (LFU)" algorithm.

* [First in First Out (FIFO)](#fifo) : In a First in First Out (FIFO) cache memory, the page that is evicted is the one that has the longest time since it was added.

Least Frequently Used (LFU)
* [Least Frequently Used (LFU)](#lfu) : In a Least Frequently Used (LFU) cache memory, the page that is evicted is the page that has had the fewest requests so far. In case of two pages having the same amount of requests, the lowest numbered page should be evicted. The number of requests that a page has had is maintained throughout the parsing of the whole set of requests, and it is not "forgotten" once a page has been removed from the cache memory.
