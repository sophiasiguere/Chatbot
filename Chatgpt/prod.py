import openai

# Configura tu clave de API
openai.api_key = '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'

# Sube el archivo JSONL
file_upload = openai.File.create(file=open("prueba.jsonl", "rb"), purpose="fine-tune")
print("Uploaded file id", file_upload.id)

while True:
    print("Waiting for file to process...")
    file_handle = openai.File.retrieve(id=file_upload.id)
    if len(file_handle) and file_handle.status == "processed":
        print("File processed")
        break

# Crea un trabajo de fine-tuning
job = openai.FineTuningJob.create(training_file=file_upload.id, model="gpt-3.5-turbo")

while True:
    print("Waiting for fine-tuning to complete...")
    job_handle = openai.FineTuningJob.retrieve(id=job.id)
    if job_handle.status == "succeeded":
        print("Fine-tuning complete")
        print("Fine-tuned model info", job_handle)
        print("Model id", job_handle.fine_tuned_model)
        break

# Reemplaza 'your_fine_tuned_model_id' con el ID real de tu modelo fine-tuneado
fine_tuned_model_id = job_handle.fine_tuned_model.id

# Crea una sesión con tu modelo fine-tuneado (text-davinci-003)
session = openai.ChatCompletion.create(
    model=fine_tuned_model_id,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ]
)

# Puedes iniciar una conversación preguntando sobre un producto específico
user_message = "Háblame sobre Decis Evo®"
response = session['choices'][0]['message']['content']
print("Respuesta del modelo:", response)

# Luego, puedes hacer más preguntas relacionadas
user_message = "¿Cuáles son los ingredientes activos de Decis Expert®?"
session = openai.ChatCompletion.create(
    model=fine_tuned_model_id,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]
)

response = session['choices'][0]['message']['content']
print("Respuesta del modelo:", response)

# Continúa haciendo preguntas de la misma manera según tus necesidades
