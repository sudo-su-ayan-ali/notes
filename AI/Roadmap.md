## Generative AI Course Roadmap

### Module 0: The Prerequisites (1-2 Months)

You can't build a great house on a weak foundation. These are non-negotiable skills.

**1. Programming & Software Tools:**

- **Python:** The lingua franca of AI. Master it.
    - **Core Concepts:** Data structures (lists, dicts), functions, classes (OOP).
    - **Key Libraries:**
        - **NumPy:** For numerical operations and multi-dimensional arrays.
        - **Pandas:** For data manipulation and analysis.
        - **Matplotlib & Seaborn:** For data visualization.
- **Essential Tools:**
    - **Jupyter Notebooks / Google Colab:** For interactive coding and experiments.
    - **Git & GitHub:** For version control and collaboration.
    - **Command Line (Bash):** For navigating systems and running scripts.

**2. Mathematics Foundations:**

- **Linear Algebra:** The language of neural networks.
    - **Core Concepts:** Vectors, Matrices, Tensors, Dot Products, Matrix Multiplication.
    - **Why?** Neural network weights and data are stored as matrices and tensors.
- **Calculus:** The engine of learning.
    - **Core Concepts:** Derivatives, Gradients, The Chain Rule.
    - **Why?** To understand **gradient descent** and **backpropagation**, the core algorithm for training neural networks.
- **Probability & Statistics:** The framework for uncertainty.
    - **Core Concepts:** Probability distributions, Conditional Probability, Bayes' Theorem, Mean, Variance.
    - **Why?** Generative models are probabilistic by nature; they learn to model the probability distribution of data.

---

### Module 1: Foundations of Deep Learning (2-3 Months)

Generative AI is a subset of deep learning. You must master the basics first.

**1. Introduction to Machine Learning:**

- Supervised vs. Unsupervised vs. Reinforcement Learning.
- The concept of a model, loss function, and optimizer.

**2. Core Neural Networks:**

- **Artificial Neural Networks (ANNs):** Neurons, layers, activation functions (ReLU, Sigmoid).
- **Training a Neural Network:** Backpropagation and Gradient Descent.
- **Deep Learning Frameworks:** Pick one and stick with it.
    - **PyTorch (Recommended):** More Pythonic, flexible, and dominant in research.
    - **TensorFlow/Keras:** Great for production and has a simpler high-level API.

**3. Architectures for Different Data Types:**

- **Convolutional Neural Networks (CNNs):** The standard for image data. Understand convolutions and pooling.
- **Recurrent Neural Networks (RNNs & LSTMs):** The classic approach for sequence data (like text). Understand the concept of hidden states and the vanishing gradient problem.

---

### Module 2: The Generative AI Revolution Begins (2-3 Months)

Now we get to the core generative concepts.

**1. The "Attention Mechanism":**

- The core idea that revolutionized sequence modeling and replaced RNNs.
- Understand how a model can "pay attention" to different parts of an input.

**2. The Transformer Architecture:**

- Read (or watch a video on) the paper **"Attention Is All You Need."**
- **Key Concepts:** Self-Attention, Positional Encodings, Encoder-Decoder structure. This is the architectural basis for almost all modern LLMs.

**3. Introduction to Large Language Models (LLMs):**

- **Pre-training:** How models learn general knowledge from massive amounts of text data (e.g., the whole internet).
- **Fine-tuning:** How to adapt a pre-trained model for a specific task (e.g., instruction following).
- **Key Architectures:**
    - **GPT (Decoder-only):** The foundation of models like ChatGPT, used for text generation.
    - **BERT (Encoder-only):** Used for understanding text (e.g., classification, search).
    - **T5 (Encoder-Decoder):** Used for sequence-to-sequence tasks (e.g., translation).

---

### Module 3: Practical LLM Application & Engineering (2-3 Months)

Theory is great, but real-world value comes from application.

**1. Using LLMs via APIs:**

- Get comfortable with APIs from **OpenAI**, **Anthropic (Claude)**, **Google (Gemini)**, or open-source models via **Hugging Face**.

**2. Prompt Engineering:**

- The art and science of writing effective prompts.
- **Techniques:** Zero-shot, Few-shot prompting, Chain-of-Thought (CoT), role-playing.

**3. Fine-Tuning Open-Source Models:**

- Learn how to fine-tune models like **Llama 3**, **Mistral**, or **Phi-3** on your own data.
- **Techniques:** Full fine-tuning vs. Parameter-Efficient Fine-Tuning (**PEFT**), especially **LoRA** and **QLoRA**.

**4. Retrieval-Augmented Generation (RAG):**

- The most common pattern for building applications with LLMs.
- **Vector Embeddings:** How to represent text as numbers.
- **Vector Databases:** Storing and retrieving information (e.g., Pinecone, Chroma, FAISS).
- **Frameworks:** **LangChain** and **LlamaIndex** to orchestrate RAG pipelines.

---

### Module 4: Beyond Text - Images, Audio, and Multimodality (2-3 Months)

Generative AI is not just about language.

**1. Generative Models for Images:**

- **Generative Adversarial Networks (GANs):** The classic "generator vs. discriminator" model. (Good to know historically).
- **Diffusion Models (The State-of-the-Art):** The technology behind **DALL-E 3**, **Midjourney**, and **Stable Diffusion**.
    - **Concept:** Start with pure noise and gradually denoise it into a coherent image guided by a text prompt.

**2. Multimodal Models:**

- Models that understand more than one type of data (e.g., text and images).
- **Key Concepts:** **CLIP** (how to connect images and text).
- **Examples:** **GPT-4V** (vision), **Sora** (video generation).

**3. Generative Audio & Music:**

- Explore models that can generate human-like speech, sound effects, or music.

---

### Module 5: The Frontier - Advanced Topics (Ongoing)

This is where you go from practitioner to expert.

**1. Aligning Models with Human Values:**

- **Reinforcement Learning from Human Feedback (RLHF):** The technique used to make models like ChatGPT helpful and harmless.
- **Direct Preference Optimization (DPO):** A newer, more direct method for alignment.

**2. AI Agents & Tool Use:**

- Moving beyond Q&A to LLMs that can take actions, use tools (like calculators or APIs), and solve multi-step problems.

**3. Model Efficiency:**

- **Quantization:** Making models smaller and faster by reducing the precision of their weights.
- **Mixture of Experts (MoE):** An architecture (used in Mixtral and GPT-4) where only parts of the model are used for any given input, making it more efficient.

---
