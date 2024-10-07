# lab2/views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from django.http import HttpResponse

def home(request):
    # Form cho người dùng nhập câu
    form = """
    <h1>Chào mừng đến với ứng dụng phân tích tâm trạng!</h1>
    <form method="post" action="/analyze_sentiment/">
        <textarea name="text" rows="4" cols="50" placeholder="Nhập câu của bạn ở đây..."></textarea><br>
        <input type="submit" value="Phân tích tâm trạng">
    </form>
    """
    return HttpResponse(form)

@csrf_exempt
def analyze_sentiment(request):
    if request.method == "POST":
        # Lấy văn bản từ request
        text = request.POST.get('text')

        # Đọc dữ liệu
        data = pd.read_csv(r"/Users/nguyenngocbaotram/Documents/HM&UD/LAB2-MachineLearning/LAB2-MachineLearning/Data/Education.csv")
        X = data['Text']
        y = data['Label'].map({'positive': 1, 'negative': 0})

        # Tiền xử lý dữ liệu
        vectorizer = CountVectorizer(stop_words='english', binary=True)
        X_vectorized = vectorizer.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

        # Huấn luyện mô hình
        ber_nb = BernoulliNB()
        ber_nb.fit(X_train, y_train)
        mul_nb = MultinomialNB()
        mul_nb.fit(X_train, y_train)

        # Dự đoán cho văn bản mới
        text_vectorized = vectorizer.transform([text])
        prediction_bernoulli = ber_nb.predict(text_vectorized)[0]
        prediction_multinomial = mul_nb.predict(text_vectorized)[0]

        # Kết quả
        results = f"""
        <h2>Kết quả phân tích tâm trạng cho văn bản: '{text}'</h2>
        <h3>Dự đoán của Bernoulli Naive Bayes: {'positive' if prediction_bernoulli == 1 else 'negative'}</h3>
        <h3>Dự đoán của Multinomial Naive Bayes: {'positive' if prediction_multinomial == 1 else 'negative'}</h3>
        <a href='/'>Quay lại</a>
        """

        return HttpResponse(results)
    else:
        return HttpResponse("<h2>Chỉ chấp nhận phương thức POST.</h2>")
