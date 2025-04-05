import requests
import yaml

# Hàm gửi yêu cầu API
def send_api_request(question, exam_id="67f125fa7999aff077949907"):
    url = 'http://localhost:5000/v1/question/create'  # URL của API
    data = {
        'question_text': question['question_text'],
        'options': question['options'],
        'correct_option': question['correct_option'],
        'question_img': question['question_img'],
        'explanation': question['explanation'],
        'examId': exam_id
    }
    
    # Gửi yêu cầu POST
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print("API call successful!")
        print(response.json())  # In ra phản hồi từ API
    else:
        print(f"Failed to call API. Status code: {response.status_code}")
        print(response.text)

# Hàm đọc câu hỏi từ file input.txt
def read_questions_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    questions = content.strip().split("\n\n")
    question_list = []

    for question in questions:
        question_data = yaml.safe_load(question)
        question_list.append(question_data)
    
    return question_list

if __name__ == "__main__":
    file_path = 'input.txt'  # Đường dẫn tới file input.txt
    questions = read_questions_from_file(file_path)

    for question in questions:
        # Gọi API với từng câu hỏi
        send_api_request(question)
