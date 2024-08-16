# **Chatbot Using OLLAMA**

Welcome to the **Chatbot** repository, built using Llama 2, LangChain, and Ollama. The chatbot developed in this project, named Zenith, offers insightful and helpful responses to queries related to lifestyle, health, skincare, diet, and more.

## **Features**

- **Interactive Chat Interface**: Easily engage with the chatbot through a user-friendly Streamlit interface.
- **Tailored AI Responses**: Powered by a custom Llama 2 model designed to provide thoughtful answers on a range of lifestyle topics.
- **Session Persistence**: Chat history is maintained, allowing you to continue conversations seamlessly.

## **Getting Started**

### **Prerequisites**

Before running this application, ensure you have the following installed:

- **Python 3.8 or higher**
- **Pip** (Python package manager)
- - **To create and run your model check below** ( [Creating and Running the Model](#creating-and-running-the-model) )


### **Installation**

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/JyothiYaga/Chatbot-using-OLLAMA.git
   cd Chatbot-using-OLLAMA
   ```

2. **Install Required Packages**

   Install the necessary Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

### **Running the Application**

To start the chatbot application, execute the following command in your terminal:

```bash
streamlit run app.py
```

This will launch the Streamlit app, and you can start interacting with the chatbot directly from your web browser.

## **Project Structure**

- **app.py**: The main file containing the Streamlit code to render the chat interface.
- **llama2.py**: Handles the interaction with the custom Llama 2 model through Ollama.
- **model file**: Defines the model parameters and the system prompt that guide the chatbot's behavior.
- **requirements.txt**: Lists all the Python dependencies required to run the application.

## **Customization**

The model's behavior can be customized by editing the `model file`. You can change the system prompt, adjust temperature settings, or modify other parameters to tailor the chatbot's responses to your needs.


## **Creating and Running the Model** 

To create and run the model, follow these steps:

1. **Open the Project in the Terminal**

   - Navigate to your project directory in the terminal.

2. **Create the Model**

   - After creating the `modelfile`, run the following command to create the model:

     ```bash
     ollama create <yourmodelname> -f modelfile
     ```

   - Replace `<yourmodelname>` with the desired name for your model. This command will create a model using the configurations in your `modelfile`.

3. **Run the Model**

   - To check if the model is working, you can run the following command:

     ```bash
     ollama run <yourmodelname>
     ```

   - This will execute the model with the name you specified and allow you to interact with it.

## **Contributing**

We welcome contributions! If you have any ideas for improvements or new features, feel free to submit a pull request or open an issue.


## **Acknowledgments**

- **Streamlit**: For providing the framework to create an interactive web interface.
- **LangChain & Ollama**: For enabling seamless integration with AI models.
- **Llama 2**: The powerful AI model behind the chatbot's responses.
- I would like to extend my gratitude to [Mr. Krish Naik](https://youtube.com/@krishnaik06?si=nZrTxowY0PlUFc_y) for their excellent tutorial that greatly assisted in the creation of this project. Their guidance and expertise were invaluable in helping me understand and implement the key concepts involved in building this chatbot.
