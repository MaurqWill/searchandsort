from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/sort_videos', methods=['GET'])
def get_sorted_videos():
    video_titles = [
        "The Art of Coding",
        "Exploring the Cosmos",
        "Cooking Masterclass: Italian Cuisine",
        "History Uncovered: Ancient Civilizations",
        "Fitness Fundamentals: Strength Training",
        "Digital Photography Essentials",
        "Financial Planning for Beginners",
        "Nature's Wonders: National Geographic",
        "Artificial Intelligence Revolution",
        "Travel Diaries: Discovering Europe"
    ]
    sorted_videos = merge_sort(video_titles)
    return jsonify(sorted_videos)





def merge_sort(video_titles):
    if len(video_titles) > 1:
        print(video_titles)  # Debugging statement
        
        mid = len(video_titles) // 2
        left_side = video_titles[:mid]
        right_side = video_titles[mid:]

        merge_sort(left_side)
        merge_sort(right_side)
        print(f'Merging {left_side} and {right_side}')  # Debugging statement

        i = j = k = 0

        while j < len(left_side) and k < len(right_side):
            if left_side[j] < right_side[k]:
                video_titles[i] = left_side[j]
                j += 1
            else:
                video_titles[i] = right_side[k]
                k += 1
            i += 1

        while j < len(left_side):
            video_titles[i] = left_side[j]
            j += 1
            i += 1

        while k < len(right_side):
            video_titles[i] = right_side[k]
            k += 1
            i += 1

        print('MERGED')  # Debugging statement
    else:
        print('BASE CASE')  # Debugging statement

    return video_titles


video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

sorted_videos = merge_sort(video_titles)
print("Sorted Videos:", sorted_videos)




if __name__ == '__main__':
    app.run(debug=True)