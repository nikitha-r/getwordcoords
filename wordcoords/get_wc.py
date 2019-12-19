import fitz


def bb_intersection_over_union(rect1, rect_set):
    output = []
    # determine the (x, y)-coordinates of the intersection rectangle
    #boxA = [row['x'], row['y'], row['x'] + row['width'], row['y'] + row['height']]
    boxA = [rect1[0], rect1[1], rect1[2], rect1[3]]
    boxes = [[rect2[0], rect2[1], rect2[2], rect2[3]] for rect2 in rect_set]
    for boxB in boxes:
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])

        # compute the area of intersection rectangle
        interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

        # compute the area of both the prediction and ground-truth
        # rectangles
        boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
        boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

        # compute the intersection over union by taking the intersection
        # area and dividing it by the sum of prediction + ground-truth
        # areas - the interesection area
        #iou = interArea / float(boxAArea + boxBArea - interArea)
        iou = interArea / float(boxAArea)
        # return the intersection over union value
        if iou > 0.9:
            output.append(True)
    return any(output)


def get_specific_word_coords(para_content, page_number, elem, fitz_doc_obj, start_index, end_index):
    specific_word_coordinates_list = []
    pre_index = 20
    if start_index > pre_index:
        updated_start_index = start_index - pre_index
    else:
        updated_start_index = start_index
    total_para_len = len(para_content)
    updated_end_index = end_index + pre_index
    mod_para_content = para_content[updated_start_index:updated_end_index]
    super_string = mod_para_content
    page = fitz_doc_obj[page_number-1]
    super_area = page.searchFor(super_string)
    text_instances = page.searchFor(elem)
    for inst in text_instances:
        if bb_intersection_over_union(inst, super_area):
            specific_word_coordinates_list = [inst[0], inst[1], inst[2], inst[3]]
            break
    return specific_word_coordinates_list


if __name__ == '__main__':
    pdf_path = "/Users/nr012/Downloads/2015-3.pdf"
    fitz_doc_obj = fitz.open(pdf_path)
    page_no = 1
    start_index, end_index = 51, 60
    para_content = "The following important factors, and other factors described elsewhere in this Report or contained in our other filings with the U.S. Securities and Exchange Commission (SEC), among others, could cause our results to differ materially from any results described in any forward-looking statements:."
    # start_index, end_index = 16, 28 #successfully in 1Page.pdf
    # para_content = "We believe that successfully meeting these objectives will generate financial performance exceeding that of our peers and result in full and fair valuation of our common shares."
    elem = para_content[start_index:end_index]
    specific_word_coordinates_list = []
    if end_index == 0:
        specific_word_coordinates_list = []
    else:
        specific_word_coordinates_list = get_specific_word_coords(para_content, page_no, elem, fitz_doc_obj, start_index, end_index)
    print(specific_word_coordinates_list)