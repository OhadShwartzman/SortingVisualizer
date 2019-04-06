import pygame
import random
import math

HEIGHT = 650
WIDTH = 1000

ARR_COUNT = 1000

BACKGROUND_COLOR = (0, 0, 0)
TILE_COLOR = (255, 255, 255)

pygame.init()
clock = pygame.time.Clock()
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.event.set_allowed([pygame.QUIT])


DISPLAY = True

DISPLAY_BARS = False


def quick_sort_update(canvas, arr):
    '''
        This function is just a wrapper for the function quicksort, to match the arguments of the 
        regular sorting functions.
        input:
            the canvas, the array
    '''
    quickSort(canvas, arr, 0, len(arr) - 1)

def partition(canvas, arr, start, end):
    '''
        This function will divide the given partition into two partitions - one which the elements are all bigger than
        or equal to the pivot value, and one in which all values are less than the pivot value
        input:
            the canvas to draw on, the array, the start index, the end index.
        output:
            the pivot index
    '''
    pivIndex = start
    pivValue = arr[end]
    for i, value in enumerate(arr[:end]):
        # Use only the range of the array between start to end.
        if i < start:
            continue
        if value < pivValue:
            arr[pivIndex], arr[i] = arr[i], arr[pivIndex]
            pivIndex += 1
            update_canvas(canvas, arr)
    arr[pivIndex], arr[end] = arr[end], arr[pivIndex]
    update_canvas(canvas, arr)
    return pivIndex
        

def quickSort(canvas, arr, start, end):
    '''
        This function will sort the array with the quicksort algorithm. a divide - conquer algorithm thing
        input:
            the canvas to draw on, the array, the start index, the end index
        output:
            none
        RECURSIVE!
    '''
    if start >= end:
        return
    div = partition(canvas, arr, start, end)
    quickSort(canvas, arr, start, div - 1)
    quickSort(canvas, arr, div + 1, end)


def shuffle_sort_update(canvas, arr):
    '''
        This function will run the shuffle sort algorithm on the array, it will put the array in a random order
        until it is sorted. it is very stupid. don't use it. It will also visualize the sorting of the array.
        input:
            the canvas, the array
        output:
            the sorted (?) array.
    '''
    flag = False
    while not flag:
        random.shuffle(arr)
        update_canvas(canvas, arr)
        flag = True
        for i, val in enumerate(arr[:-1]):
            if val > arr[i + 1]:
                flag = False
                break
    return arr

def insertion_sort_update(canvas, arr):    
    '''
        This function will run the insertion sort algorithm on the array while visuallizing it. 
        input:
            the canvas to draw on, the array to sort
        output:
            the sorted array.
    '''
    # Go over the array
    for i, key in enumerate(arr[1:]):
        j = i
        # Go backwards from the array, try and find the place where the key fits in
        while j >= 0 and key < arr[j]:
            # Move the array over by 1
            arr[j + 1] = arr[j]
            update_canvas(canvas, arr)
            j -= 1
        # This is the place where the new key fits in, put it in there.
        arr[j + 1] = key
        update_canvas(canvas, arr)
    return arr


def selection_sort_update(canvas, arr):
    '''
        This function will run the selection sort algorithm on the array, and meanwhile update the canvas to visuallize
        the current status of the array.
        input:
            the canvas to write on, the array to write from.
    '''
    flag = False
    # Run while the array is not sorted.
    while not flag:
        flag = True
        for i, val in enumerate(arr[:-1]):
            real_min = arr[i]
            index = i
            # Find the index and the value of the smallest element next to the current one.
            for j in range(i+1, len(arr)):
                if arr[j] < real_min:
                    real_min = arr[j]
                    index = j
            # If a smallest element was found, switch between the current one and this one.
            if real_min < val:
                # Flip between the elements.
                arr[index], arr[i] = arr[i], arr[index]
                update_canvas(canvas, arr)
                # Let the loop know that the array is sorted.
                flag = False
    return arr


def bubble_sort_update(canvas, arr):
    '''
        This function will run the bubble sort algorithm on the array, and meanwhile update the canvas on the 
        array's status. This algorithm is so slow, I'm currently as I'm writing this running this code and it's
        taking the longest like omg.
        input:
            the canvas to write on, the array to write from.
        output:
            the sorted array
    '''
    flag = False
    # Let the loop run as long as the array is not sorted.
    while not flag:
        flag = True
        # Go over each element in the array, look and see if it's bigger than the one next to it, if it is, 
        # Switch between them
        for i, val in enumerate(arr[:-1]):
            if val > arr[i + 1]:
                # Flip the elements
                arr[i], arr[i+1] = arr[i+1], arr[i]
                update_canvas(canvas, arr)
                # Tell the loop that it's not sorted yet.
                flag = False
    return arr

def substract_color(color1, color2):
    return (color1[0] - color2[0], color1[1] - color2[1], color1[2] - color2[2])


def update_canvas(canvas, arr):
    '''
        This function will draw a visualization of the array on the canvas. It will take each value in the array, draw it on
        the x grid relative to it's index in the array, and with the height of it's actual value.
        input:
            the canvas to draw on, the array to write from
        output:
            none
    '''
    if DISPLAY:    
        canvas.fill(BACKGROUND_COLOR)
        # Calculate the width of each rectangle in the array, since we don't always want to have as many elements in the list
        # As the width of the canvas.
        box_width = int(WIDTH / len(arr))
        # We want to see what is the difference of angle between two objects, therefore we take a full rotation
        # (2 * pi) and divide it by the number of elements in the array.
        rotational_speed = 2 * math.pi / ARR_COUNT 
        # This loop will go over each element in the list, and draw a box in the x grid of the index, and with a height of 
        # the element's value.
        for x, i in enumerate(arr):
            # Get a normalized version of the value of the element, max is 255, min is 0
            normal_i =  255 *float(i) / (HEIGHT / 2)
            # Change the color of the visual according to the value of the element.
            subs_color = (normal_i, 0, normal_i)
            rect_color = substract_color(TILE_COLOR, subs_color)
            if DISPLAY_BARS:
                pygame.draw.rect(canvas, rect_color, (x * box_width, HEIGHT - i, box_width, i), 0)
            else:
                angle = x * rotational_speed
                source_point = (WIDTH / 2, HEIGHT / 2)
                length =  i 
                dest_point = (WIDTH / 2 + math.sin(angle) * length, HEIGHT / 2 + math.cos(angle) * length)
                pygame.draw.line(canvas, rect_color, source_point, dest_point)
        pygame.display.flip()
    event_list = pygame.event.get()
    # This loop will check if the user wishes to quit the program.
    for event in event_list:
        if event.type == pygame.QUIT:
            quit()

def initialize_array(length, minimum = 0, maximum = 100):
    '''
        This function will initiallize an array with random data, which will be the array to test on in this
        program.
        input:
            the length of the array, the minimum value and the maximum value.
        output: 
            an array with random values between min and max at the chosen length
    '''
    res = []
    for i in range(length):
        res.append(random.randint(minimum, maximum))
    return res


def main():
    '''
        This is the main function of the program. This program will use pygame to visuallize sorting 
        algorithms with big random data.
    '''
    global DISPLAY
    arr = initialize_array(ARR_COUNT, 1, HEIGHT / 2)
    quick_sort_update(canvas, arr)
    DISPLAY = True # Toggle the flag that will tell the function to display the array on the screen.
    update_canvas(canvas, arr)
    # After the array has been sorted, wait until the user wants to quit the program.
    while True:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                quit()


main()