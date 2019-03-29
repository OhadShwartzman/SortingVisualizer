import pygame
import random


HEIGHT = 500
WIDTH = 1000

ARR_COUNT = 100

BACKGROUND_COLOR = (0, 0, 0)
TILE_COLOR = (255, 255, 255)

pygame.init()
clock = pygame.time.Clock()
canvas = pygame.display.set_mode((WIDTH, HEIGHT))

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

def update_canvas(canvas, arr):
    '''
        This function will draw a visualization of the array on the canvas. It will take each value in the array, draw it on
        the x grid relative to it's index in the array, and with the height of it's actual value.
        input:
            the canvas to draw on, the array to write from
        output:
            none
    '''
    canvas.fill(BACKGROUND_COLOR)
    # Calculate the width of each rectangle in the array, since we don't always want to have as many elements in the list
    # As the width of the canvas.
    box_width = int(WIDTH / len(arr))
    # This loop will go over each element in the list, and draw a box in the x grid of the index, and with a height of 
    # the element's value.
    for x, i in enumerate(arr):
        pygame.draw.rect(canvas, TILE_COLOR, (x * box_width, HEIGHT - i, box_width, i), 0)

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
    arr = initialize_array(ARR_COUNT, 1, HEIGHT)
    insertion_sort_update(canvas, arr)
    # After the array has been sorted, wait until the user wants to quit the program.
    while True:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                quit()


main()