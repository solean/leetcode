
def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    a_area = (ay2 - ay1) * (ax2 - ax1)
    b_area = (by2 - by1) * (bx2 - bx1)

    x_overlap = min(ax2, bx2) - max(ax1, bx1)
    y_overlap = min(ay2, by2) - max(ay1, by1)

    overlap_area = 0
    if x_overlap > 0 and y_overlap > 0:
        overlap_area = x_overlap * y_overlap

    return a_area + b_area - overlap_area