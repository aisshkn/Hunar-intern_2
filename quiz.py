from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Quiz questions
quiz_questions = [
    {"question": "What is the capital of France?", "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"], "answer": "C"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"], "answer": "B"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A) Charles Dickens", "B) George Orwell", "C) William Shakespeare", "D) Mark Twain"], "answer": "C"},
    {"question": "What is the largest ocean on Earth?", "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"], "answer": "D"}
]

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for i, question in enumerate(quiz_questions):
            selected_answer = request.form.get(f'question_{i}')
            if selected_answer == question["answer"]:
                score += 1
        return redirect(url_for('result', score=score))

    return render_template_string('''
        <h1>Quiz Time!</h1>
        <form method="post">
            {% for question in quiz_questions %}
                <h3>Question {{ loop.index }}: {{ question['question'] }}</h3>
                {% for option in question['options'] %}
                    <input type="radio" name="question_{{ loop.index0 }}" value="{{ option[0] }}"> {{ option }}<br>
                {% endfor %}
                <br>
            {% endfor %}
            <input type="submit" value="Submit Quiz">
        </form>
    ''', quiz_questions=quiz_questions)


@app.route('/result')
def result():
    score = request.args.get('score', 0, type=int)
    return render_template_string('''
        <h1>Quiz Over! Your final score is {{ score }}/{{ total_questions }}</h1>
        {% if score == total_questions %}
            <p>Excellent work! You got all the answers correct!</p>
        {% elif score >= total_questions / 2 %}
            <p>Good job! You did well.</p>
        {% else %}
            <p>Keep practicing! You'll get better with time.</p>
        {% endif %}
        <a href="{{ url_for('quiz') }}">Play Again</a>
    ''', score=score, total_questions=len(quiz_questions))

if __name__ == "__main__":
    app.run(debug=True)
