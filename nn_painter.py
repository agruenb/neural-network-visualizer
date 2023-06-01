import math

def paintNN(canvas, neuralNetwork, derivatives_weights, derivatives_biases):

    nnOffset = 50
    ballSize = 80
    ballPaddingX = 240
    ballPaddingY = 140
    text_size = 14
    text_position = 0.64

    text_color = "black"

    ball_centoids = []
    
    def draw_circle(canvas, x, y, radius, color):
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)

    maxLayerSize = 0
    for i in range(0, len(neuralNetwork.layers)):
        maxLayerSize = len(neuralNetwork.layers[i]) if len(neuralNetwork.layers[i]) > maxLayerSize else maxLayerSize
    #column balls
    for i in range(0, len(neuralNetwork.layers)):
        ball_centoids.append([])
        evenNodes = len(neuralNetwork.layers[i]) % 2
        columnOffset = ballSize/2 + ballPaddingY/2 if evenNodes != maxLayerSize%2 else 0
        ballDifference = maxLayerSize - len(neuralNetwork.layers[i])
        columnOffset += math.floor(ballDifference/2)*(ballSize+ballPaddingY) if ballDifference > 0 else 0
        #each ball
        for j in range(0, len(neuralNetwork.layers[i])):
            x = nnOffset + (ballSize + ballPaddingX)*i
            y = nnOffset + (ballSize + ballPaddingY)*j + columnOffset
            draw_circle(canvas, x, y, ballSize/2, "white")
            ball_centoids[i].append({
                "x":x,
                "y":y
            })
            #paint value
            ball_centoid = ball_centoids[i][j]
            node_value = str(round(neuralNetwork.layers[i][j].value, 3))
            canvas.create_text(ball_centoid.get("x"), ball_centoid.get("y"), text=node_value, fill = text_color, font=("Arial", text_size)) 

    #lines & weights
    for i in range(0, len(ball_centoids) - 1):
        # biases
        layer_bias = neuralNetwork.biases[i+1]
        offset = (ballSize+ballPaddingX)*i
        canvas.create_text(offset + nnOffset + ballPaddingX/2, nnOffset-ballSize/2, text="b"+str(i+1)+"= "+str(layer_bias), fill = text_color, font=("Arial", text_size))
        #bias change
        der = round(derivatives_biases[i], 3)
        canvas.create_text(offset + nnOffset + ballPaddingX/2, nnOffset-ballSize/2 + text_size + 4, text="upd "+str(der), fill = "red", font=("Arial", text_size))
        for j in range(0, len(ball_centoids[i])):
            ball_centoid = ball_centoids[i][j]
            out_x = ball_centoid.get("x") + ballSize/2
            #connect to each ball of next layer
            for k in range(0, len(ball_centoids[i + 1])):
                #connecting line
                next_ball_centoid = ball_centoids[i + 1][k]
                next_in_x = next_ball_centoid.get("x") - ballSize/2
                next_in_y = next_ball_centoid.get("y")
                canvas.create_line(out_x, ball_centoid.get("y"), next_in_x, next_in_y, fill="blue", width=2)
                #weight script
                middle_point_vctr_x = (next_in_x - out_x)
                middle_point_vctr_y = (next_in_y - ball_centoid.get("y"))
                middle_point_vctr_length = math.sqrt(middle_point_vctr_x**2 + middle_point_vctr_y**2)
                text_shift_y = -text_size if ball_centoid.get("y") <= next_in_y else text_size
                text_shift_x = 5
                #create text
                text_start_x = out_x + middle_point_vctr_x*text_position + text_shift_x
                text_start_y = ball_centoid.get("y") + middle_point_vctr_y*text_position + text_shift_y
                canvas.create_text(text_start_x, text_start_y, text="w", fill = text_color, font=("Arial", text_size))
                canvas.create_text(text_start_x + 13, text_start_y + 5, text=str(j+1)+str(k+1), fill = text_color, font=("Arial", int(text_size*0.7)))
                canvas.create_text(text_start_x + 13, text_start_y - 5, text="L" + str(i+1), fill = text_color, font=("Arial", int(text_size*0.7)))
                #node weights
                weight = str(neuralNetwork.layers[i + 1][k].weights[j])
                canvas.create_text(text_start_x + 20, text_start_y, text=" = "+weight, fill = text_color, font=("Arial", text_size), anchor="w")
                #node derivative
                der = 0
                #switch k and j since backpropagation orders by right nodes and this by left nodes
                der = round(-derivatives_weights[i][k][j], 3)
                canvas.create_text(text_start_x + 20, text_start_y - (text_size + 4), text="upd "+str(der), fill = "red", font=("Arial", text_size), anchor="w")

    #outputs
    for i in range(0, len(neuralNetwork.targets)):
        last_line = len(neuralNetwork.layers)-1
        text = str(neuralNetwork.targets[i])
        canvas.create_text(ball_centoids[last_line][i].get("x") + ballSize/2 + 20, ball_centoids[last_line][i].get("y"), text=text, font=("Arial", text_size), anchor="w")