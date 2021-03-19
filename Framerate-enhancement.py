import cv2
import numpy as np


def interpolate_frame(prev_frame, coords, flow):

    new_coords = coords + 0.5 * flow

    empty_locations = []
    inter_frame = cv2.remap(prev_frame, new_coords, None, cv2.INTER_LINEAR)

    # get empty pixels coordinates to check
    empty_locations = np.argwhere((inter_frame == [0, 0, 0]).all(axis=2))

    inpainted_frame = inpaint_frame(inter_frame)

    return inpainted_frame


def inpaint_frame(frame):
    
    mask = create_mask(frame)
    inpainted_frame = cv2.inpaint(frame, mask, 20, cv2.INPAINT_TELEA)
    
    return inpainted_frame


def create_mask(frame):
        
    mask = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Create mask of all pixels that are empty
    mask_values = np.where(mask == 0)
    rest = np.where(mask != 0)

    # Color the pixels in the mask
    mask[mask_values] = 255
    mask[rest] = 0

    return mask


cap = cv2.VideoCapture("Paris - 8132.mp4")

# previous fps value
fps = cap.get(cv2.CAP_PROP_FPS)
#get frame
ret, prvs_original = cap.read()

# get size
height, width, layer = prvs_original.shape
size = (width, height)

#get coordinate matrix
y_coords, x_coords = np.mgrid[0:height, 0:width]
coords = np.float32(np.dstack([x_coords, y_coords]))


prvs = cv2.cvtColor(prvs_original, cv2.COLOR_BGR2GRAY)

out = cv2.VideoWriter('Paris - 8132_enhanced.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps*2, size)


while 1:
    not_empty, next_original = cap.read()
    if not_empty:
    
        next = cv2.cvtColor(next_original, cv2.COLOR_BGR2GRAY)
        
        flow = cv2.calcOpticalFlowFarneback(next, prvs, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mid_frame = interpolate_frame(prvs_original, coords, flow)

        out.write(prvs_original)
        out.write(mid_frame)

        prvs_original = next_original
        prvs = next
    else:
        break

out.release()
cap.release()
