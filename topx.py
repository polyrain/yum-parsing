# Using a Heap here with inbuilt tools, will break this down soon
import heapq, argparse

def calculate_top_x(x: int, path: str) -> None:
    """Calculate the top x numbers in the given file, path.
    We iterate each line of the file, parsing it as an integer
    and confirming if its value is bigger than the smallest element
    in our current list. We use a Heap to back this since it has O(log(n))
    insertion and O(1) deletion, giving us a runtime complexity of O(n*log(x)),
    where x is the size of the heap required and n is the number of lines in the file.
    Finally, we sort the array which yields a runtime complexity of O(x*log(x)) where x is
    again the number of elements in the heap. This is potentially smaller than the complexity of
    parsing the file, so doesn't impact our final runtime complexity.

    As we only keep X elements in memory at any given point, the space complexity of this
    solution is O(x), where x is the size of the heap. 
    
    Algorithimically, I am unsure if we could do better; maybe some crazy DS&A that I haven't
    encountered :-) We could try and parallelise the processing of the list elements to parse
    the file faster with a worker thread handling the final heap construction, to try and 
    improve the real world performance. Might be room for improvements on the final sort as well
    since we know they're integers (assumed no floats), so could do a radix sort. 
    """
    heap = []
    with open(path, 'r') as numbers:
        try:
            for line in numbers:
                if line.isspace():
                    continue
                if len(heap) < x:
                    heapq.heappush(heap, int(line))
                elif (new_val := int(line)) > heap[0]: # We've reached a heap of X elements. If we still are processing, we now need to check if the element is bigger than the root; ie bigger than smallest
                    heapq.heappushpop(heap, new_val)
                # Otherwise, it was smaller than smallest, so don't bother                    
        except ValueError:
            print('Invalid text input in file. Please provide only single integers on each line.')   
            exit(1)
    
    # Once we're here, we can simply sort the heap to a normal list and return it
    return sorted(heap, reverse=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog = 'topX',
                    description = 'Calculates X biggest numbers in a textfile')
    parser.add_argument('number', type=int)
    parser.add_argument('filename')
    args = parser.parse_args()
    print(calculate_top_x(args.number, args.filename))
