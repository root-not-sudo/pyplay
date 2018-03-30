import statistics


def boxBlur(image):
    output = []
    for i in range(len(image)-2):
        output.append([])
        for j in range(len(image[0])-2):
            # k = statistics.mean([i, j])
            k = math.floor(statistics.mean([image[i][j], image[i][j+1], image[i][j+2], image[i+1][j],
                                            image[i+1][j+1], image[i+1][j+2], image[i+2][j], image[i+2][j+1], image[i+2][j+2]]))
            output[i].append(k)
    return output
