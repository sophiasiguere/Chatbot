from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = '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'
conversation = []

# Cargar conversaciones previas desde el archivo CSV
def cargar_conversaciones_desde_csv():
    with open('prueba.csv', 'r') as csv_file:
        for line in csv_file:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                prompt, completion = parts[0], parts[1]
                conversation.append({"role": "user", "content": prompt})
                conversation.append({"role": "assistant", "content": completion})

cargar_conversaciones_desde_csv()

# Endpoint para enviar un mensaje del usuario
@app.route('/user', methods=['POST'])
def user_message():
    
    data = request.get_json()
    user_input = data['user_input']
    conversation.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    assistant_response = response['choices'][0]['message']['content']
    conversation.append({"role": "assistant", "content": assistant_response})

    return jsonify({"assistant_response": assistant_response})

if __name__ == '__main__':
    app.run(debug=True)
