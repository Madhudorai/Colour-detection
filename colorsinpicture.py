import cv2
import pandas as pd
#image path can be changed for different images user wants
img = cv2.imread(r"C:\Users\dkaly\Downloads\pooh.jpg")

# declaring global variables (are used later on)
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv("https://github.com/Madhudorai/Colour-detection/blob/main/colors.csv", names=index, header=None)


# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    y = []
    for i in range(len(csv)):
        d = abs(B - int(csv.loc[i, "B"])) + abs(G - int(csv.loc[i, "G"])) + abs(R - int(csv.loc[i, "R"]))
        y.append(d)
    d_min = min(y)
    cname_index = y.index(d_min)
    cname = csv.loc[cname_index, "color_name"]
    return cname

# function to get b,g,r values of mouse double click
def draw_values(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

while True:
    cv2.imshow("image", img)
    cv2.setMouseCallback('image', draw_values)
    if clicked:

        # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        if r + g + b >= 600: # For light colours we will display text in black colour
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        else: #dark colours display text in white
            cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        clicked = False

    # Break the loop when user hits 'q' key
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()