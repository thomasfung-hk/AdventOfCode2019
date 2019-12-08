def parseInput(input):
    return open(input).readline().strip()

def partOneSolver(image_data):
    width = 25
    height = 6
    layer_size = width*height
    fewest_zeros = float('inf')
    answer = -1
    top_left_pixel = 0
    while top_left_pixel <= len(image_data) - layer_size:
        layer = image_data[top_left_pixel:top_left_pixel + layer_size]
        if layer.count('0') < fewest_zeros:
            fewest_zeros = layer.count('0')
            answer = layer.count('1') * layer.count('2')
        top_left_pixel += layer_size
    return answer

def partTwoSolver(image_data):
    width = 25
    height = 6
    layer_size = width*height
    final_image = '2' * layer_size
    top_left_pixel = 0
    while top_left_pixel <= len(image_data) - layer_size and final_image.count('2') != 0:
        layer = image_data[top_left_pixel:top_left_pixel + layer_size]
        for i, ch in enumerate(layer):
            if final_image[i] == '2' and layer[i] != '2':
                image_list = list(final_image)
                image_list[i] = layer[i]
                final_image = ''.join(image_list)
        top_left_pixel += layer_size
    return final_image

def visualize(final_image):
    width = 25
    height = 6
    left_pixel = 0
    while left_pixel <= width*height - width:
        row = final_image[left_pixel:left_pixel + width]
        row = row.replace('0', '■')
        row = row.replace('1', '□')
        row = row.replace('2', ' ')
        print(row)
        left_pixel += width

def main():
    image_data = parseInput('input.txt')
    print(partOneSolver(image_data))
    visualize(partTwoSolver(image_data))

if __name__ == '__main__':
    main()
